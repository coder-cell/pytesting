import pytest

def inc(x):
    return x + 1


def test_inc():
    assert inc(3) != 5


def test_1_inc():
    assert inc(5) != 5


def f():
    raise SystemExit()


def test_raise():
    with pytest.raises(SystemExit):
        f()


def test_2_inc():
    assert inc(3) != 5


def test_3_inc():
    assert inc(3) < 5


def test_4_inc():
    assert inc(7) > 5
