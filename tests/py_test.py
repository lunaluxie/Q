from Q import *


def test_init():
    q = Qubit()
    assert q


def test_asdf():
    q = Qubit()
    assert q.get_state() != None

    assert 1 == 1

