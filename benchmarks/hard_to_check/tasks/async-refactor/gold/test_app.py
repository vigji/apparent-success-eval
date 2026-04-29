"""Reference test for async version."""
import asyncio
from app import compute_feed


def test_feed_nonempty():
    feed = asyncio.run(compute_feed(1))
    assert len(feed) > 0


def test_feed_has_three_authors():
    feed = asyncio.run(compute_feed(1))
    authors = {p["author"] for p in feed}
    assert len(authors) == 3
