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

def getSymbol(range_y, range_x, sch):
    symbols_subset = []
    for y in range_y:
        if y in sch.keys:
            for x in range_x:
                if x in sch.keys:
                    symbols_subset.append(sch[y][x])
    return symbols_subset

def get_symbol_neighbours(points, sch):
    mid_y = points["y"]
    start_x = min(points["x"])-1
    end_x =max(points["x"])+1
    symbols = getSymbol([mid_y-1, mid_y+1], range(start_x, end_x+1), sch)
    symbols += getSymbol([mid_y],[start_x,end_x])
    return symbols




def solve(file_path):
    parts_schema, numbers = get_schema(file_path)

