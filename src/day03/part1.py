import os


def get_schema(file_path):
    with open(file_path) as input_file:
        numbers = []
        number_points = []
        parts_schema = {}
        y = 0
        x = 0
        number = 0
        for line in input_file:
            for character in line.strip():
                if character.isdigit():
                    number = number * 10 + int(character)
                    number_points.append(x)
                else:
                    if character != ".":
                        if y not in parts_schema.keys():
                            parts_schema[y] = {}
                        parts_schema[y][x] = character
                    if number != 0:
                        numbers.append(
                            {"number": number, "points": {"y": y, "x": number_points}}
                        )
                    number = 0
                    number_points = []
                x += 1
            if number != 0:
                numbers.append(
                    {"number": number, "points": {"y": y, "x": number_points}}
                )
            number = 0
            number_points = []
            x = 0
            y += 1
    return parts_schema, numbers


def contains_symbol(range_y, range_x, sch):
    for y in range_y:
        if y in sch.keys():
            for x in range_x:
                if x in sch[y].keys():
                    return True
    return False


def has_symbol_neighbours(points, sch):
    mid_y = points["y"]
    start_x = min(points["x"]) - 1
    end_x = max(points["x"]) + 1
    if contains_symbol([mid_y - 1, mid_y + 1], range(start_x, end_x + 1), sch):
        return True
    if contains_symbol([mid_y], [start_x, end_x], sch):
        return True
    return False


def solve(file_path):
    parts_schema, numbers = get_schema(file_path)
    sum = 0
    for n in numbers:
        if has_symbol_neighbours(n["points"], parts_schema):
            sum += n["number"]
    return sum


if __name__ == "__main__":
    input_file = os.path.dirname(__file__) + "/input_day03.txt"
    print(solve(input_file))
