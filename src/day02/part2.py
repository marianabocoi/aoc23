import os


def get_cube_number(s):
    number, cube = s.split()
    return cube, int(number)


def get_cubes_from_draw(s):
    return dict([get_cube_number(x) for x in s.strip().split(r",")])


def get_draws_from_game(s):
    return [get_cubes_from_draw(x) for x in s.strip().split(";")]


def get_game(s):
    game_name, game_values = s.split(":")
    _, game_number = game_name.split()
    return {game_number.strip(): get_draws_from_game(game_values)}


def part2(file_path):
    games = []
    with open(file_path) as input_file:
        for line in input_file:
            games.append(get_game(line))
    return games


if __name__ == "__main__":
    input_file = os.path.dirname(__file__) + "/input_day02.txt"
    print(input_file)
    print(part2(input_file))
