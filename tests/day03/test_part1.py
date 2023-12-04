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
        {467: {"y": 0, "x": [0, 1, 2]}},
        {114: {"y": 0, "x": [5, 6, 7]}},
        {35: {"y": 2, "x": [2, 3]}},
        {633: {"y": 2, "x": [6, 7, 8]}},
        {617: {"y": 4, "x": [0, 1, 2]}},
        {58: {"y": 5, "x": [7, 8]}},
        {592: {"y": 6, "x": [2, 3, 4]}},
        {755: {"y": 7, "x": [6, 7, 8]}},
        {664: {"y": 9, "x": [1, 2, 3]}},
        {598: {"y": 9, "x": [5, 6, 7]}},
    ]


def test_2():
    assert d03p1.get_symbol_neighbours({"y": 5, "x": [7, 8]}, parts_schema) == ["*"]
