import os

import day03.part1 as d03p1

test_input_file = os.path.dirname(__file__) + "/test_input_p1.txt"
schema = d03p1.get_schema(test_input_file)
parts_schema, numbers = schema


def test_1():
    assert parts_schema == {
        0: {},
        1: {3: "*"},
        2: {},
        3: {6: "#"},
        4: {3: "*"},
        5: {5: "+"},
        6: {},
        7: {},
        8: {3: "$", 5: "*"},
        9: {},
    }
    assert numbers == [
        {"number": 467, "points": {"y": 0, "x": [0, 1, 2]}},
        {"number": 114, "points": {"y": 0, "x": [5, 6, 7]}},
        {"number": 35, "points": {"y": 2, "x": [2, 3]}},
        {"number": 633, "points": {"y": 2, "x": [6, 7, 8]}},
        {"number": 617, "points": {"y": 4, "x": [0, 1, 2]}},
        {"number": 58, "points": {"y": 5, "x": [7, 8]}},
        {"number": 592, "points": {"y": 6, "x": [2, 3, 4]}},
        {"number": 755, "points": {"y": 7, "x": [6, 7, 8]}},
        {"number": 664, "points": {"y": 9, "x": [1, 2, 3]}},
        {"number": 598, "points": {"y": 9, "x": [5, 6, 7]}},
    ]


def test_2():
    assert d03p1.has_symbol_neighbours({"y": 0, "x": [0, 1, 2]}, parts_schema) is True
    assert d03p1.has_symbol_neighbours({"y": 9, "x": [5, 6, 7]}, parts_schema) is True
    assert d03p1.has_symbol_neighbours({"y": 0, "x": [5, 6, 7]}, parts_schema) is False
    assert d03p1.has_symbol_neighbours({"y": 5, "x": [7, 8]}, parts_schema) is False


def test_0():
    assert d03p1.solve(test_input_file) == 4361
