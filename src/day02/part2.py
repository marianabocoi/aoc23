import os
import math


def get_cube_number(s):
    number, cube = s.split()
    return cube, int(number)


def get_cubes_from_draw(s):
    return dict([get_cube_number(x) for x in s.strip().split(r",")])


def get_max_draws_from_game(s):
    max_draw = {}
    for x in s.strip().split(";"):
        draw = get_cubes_from_draw(x)
        for cube, number in draw.items():
            if cube in max_draw.keys() and max_draw[cube] >= number:
                pass
            else:
                max_draw[cube] = number
    return max_draw


def get_game(s):
    game_name, game_values = s.split(":")
    _, game_number = game_name.split()
    # print({int(game_number.strip()): get_max_draws_from_game(game_values)})
    return (int(game_number.strip()), get_max_draws_from_game(game_values))


def matches_constraint(game_values, constraints):
    for key, value in constraints.items():
        if value < game_values[key]:
            return False
    return True


def part2(file_path):
    games_sum = 0
    with open(file_path) as input_file:
        for line in input_file:
            _, game_max_values = get_game(line)
            games_sum += math.prod(game_max_values.values())
    return games_sum


if __name__ == "__main__":
    input_file = os.path.dirname(__file__) + "/input_day02.txt"
    print(part2(input_file))
