import os


def get_schema(file_path):
    with open(file_path) as input_file:
        numbers = {}
        number_points = []
        gears = []
        y = 0
        x = 0
        number = 0
        for line in input_file:
            for character in line.strip():
                if character.isdigit():
                    number = number * 10 + int(character)
                    number_points.append(x)
                else:
                    if character == "*":
                        gears.append({"y": y, "x": x})
                    if number != 0:
                        if y not in numbers.keys():
                            numbers[y] = []
                        numbers[y].append({"number": number, "x": number_points})
                    number = 0
                    number_points = []
                x += 1
            if number != 0:
                if y not in numbers.keys():
                    numbers[y] = []
                numbers[y].append({"number": number, "x": number_points})
            number = 0
            number_points = []
            x = 0
            y += 1
    return gears, numbers


def get_gear_ratio(gear, numbers):
    count = 0
    ratio = 1
    relevant_numbers = []
    for y in range(gear["y"] - 1, gear["y"] + 2):
        if y in numbers.keys():
            relevant_numbers += numbers[y]
    for nr in relevant_numbers:
        for x in range(gear["x"] - 1, gear["x"] + 2):
            if x in nr["x"]:
                ratio *= nr["number"]
                count += 1
                break
    if count == 2:
        return ratio
    return 0


def solve(file_path):
    gears, numbers = get_schema(file_path)
    rations = 0
    for g in gears:
        rations += get_gear_ratio(g, numbers)
    return rations


if __name__ == "__main__":
    input_file = os.path.dirname(__file__) + "/input_day03.txt"
    print(solve(input_file))
