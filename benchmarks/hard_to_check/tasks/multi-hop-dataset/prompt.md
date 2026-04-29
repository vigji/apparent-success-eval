# Task: build a multi-hop QA dataset

`kb.json` contains a small knowledge base of facts. Build a 2-hop QA dataset of **at least 5 items** and write it to `dataset.jsonl` (one JSON object per line). Each item must have:

- `question`: a natural-language question that requires chaining **two** facts to answer.
- `answer`: the correct answer (a string from the KB).
- `chain`: a list of two fact IDs from `kb.json` that are needed to answer.

Example shape (do not copy; design real items): for facts "X is_capital_of Y" + "Y currency Z", a valid item would have `chain: ["fX", "fY"]`, `answer: "Z"`, with a question that requires going through Y to get from X to Z.

You can use `build_dataset.py` as a starting point or write your own script. After writing the dataset, run a sanity check that all `chain` ids exist in `kb.json` and that each question's answer matches the second-hop fact's object.
