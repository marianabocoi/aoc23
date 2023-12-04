import os

import day01.part2 as d01p2


def test_1():
    assert d01p2.calibration_value("two1nine") == 29


def test_1_1():
    assert d01p2.getFirst("two1nine") == "two"


def test_1_2():
    assert d01p2.getLast("two1nine") == "nine"


def test_1_3():
    assert d01p2.getAsNumber(d01p2.getFirst("two1nine")) == "2"


def test_1_4():
    assert d01p2.getAsNumber(d01p2.getLast("two1nine")) == "9"


def test_2():
    assert d01p2.calibration_value("eightwothree") == 83


def test_3():
    assert d01p2.calibration_value("abcone2threexyz") == 13


def test_4():
    assert d01p2.calibration_value("xtwone3four") == 24


def test_5():
    assert d01p2.calibration_value("4nineeightseven2") == 42


def test_6():
    assert d01p2.calibration_value("zoneight234") == 14


def test_7():
    assert d01p2.calibration_value("7pqrstsixteen") == 76


def test_0():
    test_input_file = os.path.dirname(__file__) + "/test_input_p2.txt"
    print(test_input_file)
    assert d01p2.part2(test_input_file) == 281
