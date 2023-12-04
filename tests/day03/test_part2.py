import os

import day03.part2 as d03p2

test_input_file = os.path.dirname(__file__) + "/test_input_p1.txt"
schema = d03p2.get_schema(test_input_file)
gears, numbers = schema


def test_1():
    assert gears == [{"y": 1, "x": 3}, {"y": 4, "x": 3}, {"y": 8, "x": 5}]
    assert numbers == {
        0: [{"number": 467, "x": [0, 1, 2]}, {"number": 114, "x": [5, 6, 7]}],
        2: [{"number": 35, "x": [2, 3]}, {"number": 633, "x": [6, 7, 8]}],
        4: [{"number": 617, "x": [0, 1, 2]}],
        5: [{"number": 58, "x": [7, 8]}],
        6: [{"number": 592, "x": [2, 3, 4]}],
        7: [{"number": 755, "x": [6, 7, 8]}],
        9: [{"number": 664, "x": [1, 2, 3]}, {"number": 598, "x": [5, 6, 7]}],
    }


def test_2():
    assert d03p2.get_gear_ratio({"y": 1, "x": 3}, numbers) == 467 * 35
    # not a gear
    assert d03p2.get_gear_ratio({"y": 4, "x": 3}, numbers) == 0
    assert d03p2.get_gear_ratio({"y": 8, "x": 5}, numbers) == 755 * 598


def test_0():
    assert d03p2.solve(test_input_file) == 467835
