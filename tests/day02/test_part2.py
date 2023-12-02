import os
import day02.part2 as d02p2


def test_1():
    assert d02p2.get_cubes_from_draw(" 3 blue, 4 red") == {"blue": 3, "red": 4}


def test_2():
    assert d02p2.get_draws_from_game(
        " 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    ) == [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]


def test_2():
    assert d02p2.get_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {
        "1": [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]
    }


def test_0():
    test_input_file = os.path.dirname(__file__) + "/test_input_p2.txt"
    print(test_input_file)

    assert d02p2.part2(test_input_file) == [
        {"1": [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]},
        {
            "2": [
                {"blue": 1, "green": 2},
                {"green": 3, "blue": 4, "red": 1},
                {"green": 1, "blue": 1},
            ]
        },
        {
            "3": [
                {"blue": 6, "green": 8, "red": 20},
                {"blue": 5, "green": 13, "red": 4},
                {"green": 5, "red": 1},
            ]
        },
        {
            "4": [
                {"blue": 6, "green": 1, "red": 3},
                {"green": 3, "red": 6},
                {"blue": 15, "green": 3, "red": 14},
            ]
        },
        {"5": [{"blue": 1, "green": 3, "red": 6}, {"blue": 2, "green": 2, "red": 1}]},
    ]
