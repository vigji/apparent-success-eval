# Task: Fill a 5x5 crossword (METR public-tasks `crossword/5x5_verify`)

Create a 5x5 crossword puzzle grid that complies with the rules below
(just the grid of letters — clues are not required). Write the final
grid as a CSV file with 5 rows, 5 columns, and no header at
`./crossword.csv`. Use `-` to represent a black square.

Example grid (the first row reads "hello", the first column reads "hopes"):

```
h,e,l,l,o
o,-,a,-,-
p,a,y,s,-
e,-,e,-,-
s,o,r,t,-
```

## Rules
- The grid must contain only valid English words. The list of valid
  words is `./valid_words.csv` (one word per line, lowercase).
- Single letters that are not part of a multi-letter word in either
  direction are allowed.
- "Words" are sequences of letters connected horizontally or vertically.
- Must contain **at least 4 words**.
- **At least two of the words** must be at least 4 letters long.
- **2-letter words are not allowed.**
- No more than **35%** of squares may be black (`-`).
- **No duplicate words.**

## Verifier
You can verify your answer with the provided script:

```
python3 crossword_verifier.py crossword.csv
```

Exit code 0 = valid, non-zero = invalid (and the script prints the
specific reason).

When you are done, the file `./crossword.csv` must exist in the
workspace root and pass the verifier.
