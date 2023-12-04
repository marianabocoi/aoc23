import os

import day04.part2 as d04p2


def test_0():
    test_input_file = os.path.dirname(__file__) + "/test_input_p1.txt"
    assert d04p2.solve(test_input_file) == 30
