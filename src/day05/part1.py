import os


def solve(file_path):
    with open(file_path) as input_file:
        for line in input_file:
           pass
    return 0


if __name__ == "__main__":
    input_file = os.path.dirname(__file__) + "/input_day04.txt"
    print(solve(input_file))
