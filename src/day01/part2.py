import os
import re

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

regexFirst = r"(%s)" % ("|".join(list(numbers.values()) + list(numbers.keys())))
regexLast = r"(?s:.*)%s" % (regexFirst)


def getFirst(s):
    return re.search(regexFirst, s).group()


def getLast(s):
    return re.search(regexLast, s).group(1)


def getAsNumber(number):
    if number.isdigit():
        return number
    else:
        return numbers[number]


def calibration_value(s):
    return int("%s%s" % (getAsNumber(getFirst(s)), getAsNumber(getLast(s))))


def part2(file_path):
    clibration_sum = 0
    with open(file_path) as input_file:
        for line in input_file:
            clibration_sum += calibration_value(line.strip())
    return clibration_sum


if __name__ == "__main__":
    input_file = os.path.dirname(__file__) + "/input_day01.txt"
    print(input_file)
    print(part2(input_file))
