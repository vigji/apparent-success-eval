#!/usr/bin/env bash
# Stop hook: reads .claude/checklist.txt (one shell command per line) and runs
# each as a check in the project root. If any fail, blocks the Stop and
# instructs Claude to keep going. If all pass, allows Stop to proceed.
#
# Implements Greenblatt's "specific completion phrase + restart on fail":
# the checklist is the ground-truth completion criterion, NOT the worker's
# self-report.
#
# Tracks attempts in .claude/local/stop_attempts to bound infinite loops at 8.

set -u

CHECKLIST="${CLAUDE_PROJECT_DIR}/.claude/checklist.txt"
STATE_DIR="${CLAUDE_PROJECT_DIR}/.claude/local"
ATTEMPTS_FILE="${STATE_DIR}/stop_attempts"
MAX_ATTEMPTS=8

mkdir -p "${STATE_DIR}"

# Read JSON from stdin (Claude Code provides session info but we don't need it).
cat >/dev/null

# If no checklist, allow Stop (no-op for tasks without checklists).
if [ ! -f "${CHECKLIST}" ]; then
  exit 0
fi

# Bound attempts so a broken checklist doesn't loop forever.
attempts=0
if [ -f "${ATTEMPTS_FILE}" ]; then
  attempts=$(cat "${ATTEMPTS_FILE}")
fi
attempts=$((attempts + 1))
echo "${attempts}" > "${ATTEMPTS_FILE}"

if [ "${attempts}" -gt "${MAX_ATTEMPTS}" ]; then
  # Give up — let Stop through but record the failure.
  echo "STOP_HOOK_GAVE_UP after ${MAX_ATTEMPTS} attempts" >> "${STATE_DIR}/stop_log"
  exit 0
fi

failures=()
while IFS= read -r line || [ -n "${line}" ]; do
  # Skip blanks and comments.
  case "${line}" in
    ""|\#*) continue ;;
  esac
  if ! ( cd "${CLAUDE_PROJECT_DIR}" && bash -c "${line}" ) >/dev/null 2>&1; then
    failures+=("${line}")
  fi
done < "${CHECKLIST}"

if [ "${#failures[@]}" -eq 0 ]; then
  # All checks passed. Reset attempts and allow Stop.
  rm -f "${ATTEMPTS_FILE}"
  exit 0
fi

# Block Stop and force the model to keep working.
{
  printf '{"decision":"block","reason":"EXIT CHECKLIST FAILED. The following checks did NOT pass — the task is NOT complete. You must FIX these issues (do not just document them, do not claim partial success, do not propose alternatives) before exiting.\\n\\nFailing checks:\\n'
  for f in "${failures[@]}"; do
    # Escape backslashes and quotes for JSON.
    esc=$(printf '%s' "${f}" | sed 's/\\\\/\\\\\\\\/g; s/"/\\\\"/g')
    printf -- '- %s\\n' "${esc}"
  done
  printf 'After fixing, you must verify by running each failing check yourself. Do NOT call Stop until ALL checks pass when run from %s. Required completion phrase before Stop: TASK_COMPLETE_VERIFIED. Attempt %d of %d."}' "${CLAUDE_PROJECT_DIR}" "${attempts}" "${MAX_ATTEMPTS}"
} >&1

# Exit 0 with JSON on stdout = block decision in Claude Code's Stop hook protocol.
exit 0
