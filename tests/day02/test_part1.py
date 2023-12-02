import os
import day02.part1 as d02p1


def test_1():
    assert d02p1.get_cubes_from_draw(" 3 blue, 4 red") == {"blue": 3, "red": 4}


def test_2():
    assert d02p1.get_max_draws_from_game(
        " 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    ) == {"blue": 6, "red": 4, "green": 2}


def test_3():
    assert (
        d02p1.matches_constraint(
            {"blue": 6, "red": 4, "green": 2}, {"blue": 6, "red": 4, "green": 2}
        )
        == True
    )
    assert (
        d02p1.matches_constraint(
            {"blue": 1, "red": 1, "green": 1}, {"blue": 6, "red": 4, "green": 2}
        )
        == True
    )
    assert (
        d02p1.matches_constraint(
            {"blue": 10, "red": 4, "green": 2}, {"blue": 6, "red": 4, "green": 2}
        )
        == False
    )
    assert (
        d02p1.matches_constraint(
            {"blue": 6, "red": 20, "green": 2}, {"blue": 6, "red": 4, "green": 2}
        )
        == False
    )


def test_0():
    test_input_file = os.path.dirname(__file__) + "/test_input_p1.txt"
    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }  # 12 red cubes, 13 green cubes, and 14 blue cub
    print(test_input_file, constraints)
    assert d02p1.part1(test_input_file, constraints) == 8
