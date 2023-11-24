import pytest
import os

from src import parseData


def test_0():
    print(os.getcwd())
    assert 1 == 2