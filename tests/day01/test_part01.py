import os
import day01.part1 as d01p1


def test_1():
    assert d01p1.calibration_value("1abc2") == 12


def test_2():
    assert d01p1.calibration_value("pqr3stu8vwx") == 38


def test_3():
    assert d01p1.calibration_value("a1b2c3d4e5f") == 15


def test_4():
    assert d01p1.calibration_value("treb7uchet") == 77


def test_5():
    test_input_file = os.path.dirname(__file__) + "/test_input.txt"
    print(test_input_file)
    assert d01p1.part1(test_input_file) == 142
