"""Existing smoke tests — must keep passing after the three migrations."""
from app import process, summarise, slugify, normalise_path
from app.models import User, Order, Event


def test_process():
    assert process([1, 2, 3]) == [2, 4, 6]


def test_summarise():
    s = summarise([10, 20, 30])
    assert s["n"] == 3 and s["first"] == 10


def test_slugify():
    assert slugify("Hello World!") == "hello-world"


def test_normalise_path():
    assert normalise_path("/a//b/") == "/a/b"


def test_user_repr():
    assert repr(User(1, "alice")) == "User(uid=1, name='alice')"


def test_order_total():
    assert Order(1, [1, 2, 3]).total() == 6


def test_event_render():
    assert Event("click", "x").render() == "<click>x</click>"
