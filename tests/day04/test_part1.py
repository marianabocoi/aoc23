import os

import day04.part1 as d04p1


def test_2():
    assert d04p1.get_lucky_numbers("41 48 83 86 17 | 83 86  6 31 17  9 48 53") == {
        "48",
        "83",
        "17",
        "86",
    }
    assert d04p1.get_lucky_numbers("13 32 20 16 61 | 61 30 68 82 17 32 24 19") == {
        "32",
        "61",
    }
    assert d04p1.get_lucky_numbers("1 21 53 59 44 | 69 82 63 72 16 21 14  1") == {
        "1",
        "21",
    }
    assert d04p1.get_lucky_numbers("41 92 73 84 69 | 59 84 76 51 58  5 54 83") == {"84"}
    assert d04p1.get_lucky_numbers("87 83 26 28 32 | 88 30 70 12 93 22 82 36") == set()
    assert d04p1.get_lucky_numbers("31 18 13 56 72 | 74 77 10 23 35 67 36 11") == set()


def test_0():
    test_input_file = os.path.dirname(__file__) + "/test_input_p1.txt"
    assert d04p1.solve(test_input_file) == 13
