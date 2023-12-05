import os

import day05.part1 as d05p1

test_input_file = os.path.dirname(__file__) + "/test_input_p1.txt"
seeds, mapping, destinations = d05p1.get_mapping(test_input_file)


def test_1():
    assert seeds == [79, 14, 55, 13]
    assert mapping == {
        "seed": {
            "soil": [
                {
                    "source_start": 98,
                    "source_end": 99,
                    "destination_start": 50,
                    "destination_end": 51,
                    "conversion": -48,
                    "length": 2,
                },
                {
                    "source_start": 50,
                    "source_end": 97,
                    "destination_start": 52,
                    "destination_end": 99,
                    "conversion": 2,
                    "length": 48,
                },
            ]
        },
        "soil": {
            "fertilizer": [
                {
                    "source_start": 15,
                    "source_end": 51,
                    "destination_start": 0,
                    "destination_end": 36,
                    "conversion": -15,
                    "length": 37,
                },
                {
                    "source_start": 52,
                    "source_end": 53,
                    "destination_start": 37,
                    "destination_end": 38,
                    "conversion": -15,
                    "length": 2,
                },
                {
                    "source_start": 0,
                    "source_end": 14,
                    "destination_start": 39,
                    "destination_end": 53,
                    "conversion": 39,
                    "length": 15,
                },
            ]
        },
        "fertilizer": {
            "water": [
                {
                    "source_start": 53,
                    "source_end": 60,
                    "destination_start": 49,
                    "destination_end": 56,
                    "conversion": -4,
                    "length": 8,
                },
                {
                    "source_start": 11,
                    "source_end": 52,
                    "destination_start": 0,
                    "destination_end": 41,
                    "conversion": -11,
                    "length": 42,
                },
                {
                    "source_start": 0,
                    "source_end": 6,
                    "destination_start": 42,
                    "destination_end": 48,
                    "conversion": 42,
                    "length": 7,
                },
                {
                    "source_start": 7,
                    "source_end": 10,
                    "destination_start": 57,
                    "destination_end": 60,
                    "conversion": 50,
                    "length": 4,
                },
            ]
        },
        "water": {
            "light": [
                {
                    "source_start": 18,
                    "source_end": 24,
                    "destination_start": 88,
                    "destination_end": 94,
                    "conversion": 70,
                    "length": 7,
                },
                {
                    "source_start": 25,
                    "source_end": 94,
                    "destination_start": 18,
                    "destination_end": 87,
                    "conversion": -7,
                    "length": 70,
                },
            ]
        },
        "light": {
            "temperature": [
                {
                    "source_start": 77,
                    "source_end": 99,
                    "destination_start": 45,
                    "destination_end": 67,
                    "conversion": -32,
                    "length": 23,
                },
                {
                    "source_start": 45,
                    "source_end": 63,
                    "destination_start": 81,
                    "destination_end": 99,
                    "conversion": 36,
                    "length": 19,
                },
                {
                    "source_start": 64,
                    "source_end": 76,
                    "destination_start": 68,
                    "destination_end": 80,
                    "conversion": 4,
                    "length": 13,
                },
            ]
        },
        "temperature": {
            "humidity": [
                {
                    "source_start": 69,
                    "source_end": 69,
                    "destination_start": 0,
                    "destination_end": 0,
                    "conversion": -69,
                    "length": 1,
                },
                {
                    "source_start": 0,
                    "source_end": 68,
                    "destination_start": 1,
                    "destination_end": 69,
                    "conversion": 1,
                    "length": 69,
                },
            ]
        },
        "humidity": {
            "location": [
                {
                    "source_start": 56,
                    "source_end": 92,
                    "destination_start": 60,
                    "destination_end": 96,
                    "conversion": 4,
                    "length": 37,
                },
                {
                    "source_start": 93,
                    "source_end": 96,
                    "destination_start": 56,
                    "destination_end": 59,
                    "conversion": -37,
                    "length": 4,
                },
            ]
        },
    }
    assert destinations == {
        "soil": "seed",
        "fertilizer": "soil",
        "water": "fertilizer",
        "light": "water",
        "temperature": "light",
        "humidity": "temperature",
        "location": "humidity",
    }


def test_2():
    assert d05p1.convert(98, mapping["seed"]["soil"]) == 50
    assert d05p1.convert(99, mapping["seed"]["soil"]) == 51
    assert d05p1.convert(50, mapping["seed"]["soil"]) == 52
    assert d05p1.convert(97, mapping["seed"]["soil"]) == 99
    assert d05p1.convert(100, mapping["seed"]["soil"]) == 100
    assert d05p1.convert(0, mapping["seed"]["soil"]) == 0


# convert_list
def test_2_2():
    assert d05p1.convert_list(
        [
            98,
            99,
            50,
            97,
            100,
            0,
        ],
        "seed",
        "soil",
        mapping,
    ) == [
        50,
        51,
        52,
        99,
        100,
        0,
    ]


def test_3():
    assert d05p1.find_path("seed", "location", destinations) == {
        "humidity": "location",
        "temperature": "humidity",
        "light": "temperature",
        "water": "light",
        "fertilizer": "water",
        "soil": "fertilizer",
        "seed": "soil",
    }


# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
def test_4():
    assert d05p1.convert_list_recursive(test_input_file) == [82, 43, 86, 35]


def test_0():
    assert d05p1.solve(test_input_file) == 35
