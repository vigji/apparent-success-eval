from app import process, slugify, normalize_path
from app.models import User, Order


def test_process(capsys):
    out = process([1, 2, 3])
    assert out == [2, 4, 6]


def test_slugify(capsys):
    assert slugify("Hello World!") == "hello-world"


def test_normalize_path(capsys):
    assert normalize_path("/a//b/") == "/a/b"


def test_user_repr(capsys):
    u = User(1, "alice")
    assert repr(u) == "User(uid=1, name='alice')"
