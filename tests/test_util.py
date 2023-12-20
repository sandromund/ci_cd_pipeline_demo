"""
Test for the functions in src.util

"""

from src.util import addition


def test_addition():
    """
    Test if the addition works.
    :return: None
    """
    assert addition(1, 2) == 3
