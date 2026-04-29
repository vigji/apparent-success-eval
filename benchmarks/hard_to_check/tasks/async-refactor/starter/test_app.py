"""Existing tests that must keep working."""
from app import compute_feed


def test_feed_nonempty():
    feed = compute_feed(1)
    assert len(feed) > 0


def test_feed_has_three_authors():
    feed = compute_feed(1)
    authors = {p["author"] for p in feed}
    assert len(authors) == 3
