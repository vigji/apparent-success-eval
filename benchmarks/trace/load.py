"""TRACE dataset loader — currently a stub.

The original TRACE dataset (PatronusAI/trace-dataset on HuggingFace) is gated
and requires HF authentication + terms acceptance. We pivoted to using the
Exp 1 trajectories as an in-distribution reward-hack detection benchmark
(see run_detection.py).

If you obtain HF access, this module can be filled in to load TRACE rows
in a format compatible with run_detection.evaluate (each row needs at minimum
a `final_message`-equivalent string and a ground-truth hack label).
"""
from __future__ import annotations

import os


def load_trace(split: str = "train"):
    if not os.environ.get("HF_TOKEN"):
        raise RuntimeError(
            "TRACE is gated. Set HF_TOKEN and accept dataset terms at "
            "https://huggingface.co/datasets/PatronusAI/trace-dataset, or "
            "use run_detection.py against Exp 1 results instead."
        )
    from datasets import load_dataset  # type: ignore
    return load_dataset("PatronusAI/trace-dataset", split=split)
