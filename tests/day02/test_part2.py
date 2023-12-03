import os
import day02.part2 as d02p2


def test_1():
    assert d02p2.get_cubes_from_draw(" 3 blue, 4 red") == {"blue": 3, "red": 4}


def test_2():
    assert d02p2.get_max_draws_from_game(
        " 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    ) == {"blue": 6, "red": 4, "green": 2}



def test_0():
    test_input_file = os.path.dirname(__file__) + "/test_input_p2.txt"
    print(test_input_file)

    assert d02p2.part2(test_input_file) == 2286