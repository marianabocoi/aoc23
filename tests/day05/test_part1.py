import os
import day04.part1 as d04p1

def test_1():
    assert d04p1.get_lucky_numbers("41 92 73 84 69 | 59 84 76 51 58  5 54 83") == {"84"}


def test_0():
    test_input_file = os.path.dirname(__file__) + "/test_input_p1.txt"
    assert d04p1.solve(test_input_file) == 13
