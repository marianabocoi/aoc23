def get_schema(file_path):
    with open(file_path) as input_file:
        numbers = []
        number_points = []
        parts_schema = {}
        y = 0
        x = 0
        number = 0
        for line in input_file:
            parts_schema[y] = {}
            for character in line.strip():
                if character.isdigit():
                    number = number * 10 + int(character)
                    number_points.append(x)
                else:
                    if character != ".":
                        parts_schema[y][x] = character
                    if number != 0:
                        numbers.append({number: {"y": y, "x": number_points}})
                    number = 0
                    number_points = []
                x += 1
            if number != 0:
                numbers.append({number: {"y": y, "x": number_points}})
            number = 0
            number_points = []
            x = 0
            y += 1
    return parts_schema, numbers


def get_symbol_neighbours(points, sch):
    symbols = []
    print('points["y"]', points)
    print('(points["y"] - 1)', (points["y"] - 1))
    if (points["y"] - 1) in sch.keys:
        if points["x"][0] - 1 in sch[points["y"] - 1].keys:
            symbols.append(sch[points["y"] - 1][points["x"][0] - 1])
        if points["x"][:-1] + 1 in sch[points["y"] - 1].keys:
            symbols.append(sch[points["y"] - 1][points["x"][:-1] + 1])
        for k in points["x"]:
            if k in sch[points["y"] - 1].keys:
                symbols.append(sch[k][points["y"] - 1])

    if points["y"] + 1 in sch.keys:
        if points["x"][0] - 1 in sch[points["y"] + 1].keys:
            symbols.append(sch[points["y"] + 1][points["x"][0] - 1])
        if points["x"][:-1] + 1 in sch[points["y"] + 1].keys:
            symbols.append(sch[points["y"] + 1][points["x"][:-1] + 1])
        for k in points["x"]:
            if k in sch[points["y"] + 1].keys:
                symbols.append(sch[k][points["y"] + 1])

        if points["x"][0] - 1 in sch[points["y"]].keys:
            symbols.append(sch[points["y"]][points["x"][0] - 1])
        if points["x"][:-1] + 1 in sch[points["y"]].keys:
            symbols.append(sch[points["y"]][points["x"][:-1] + 1])


def solve(file_path):
    parts_schema, numbers = get_schema(file_path)
