import os


def getFirst(s):
    for i in s:
        if i.isdigit():
            return i


def getLast(s):
    return getFirst(s[::-1])


def calibration_value(s):
    return int("%s%s" % (getFirst(s), getLast(s)))


def part1(file_path):
    clibration_sum = 0
    with open(file_path) as input_file:
        for line in input_file:
            value = calibration_value(line.strip())
            if value > 99:
                print(value)
            clibration_sum += value
    return clibration_sum


if __name__ == "__main__":
    input_file = os.path.dirname(__file__) + "/input_day01.txt"
    print(input_file)
    print(part1(input_file))
