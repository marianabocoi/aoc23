import os
import math

def get_lucky_numbers(card):
    winning_numbers, my_numbers = [set(x.split()) for x in card.split(" | ")]
    # set intersection
    return winning_numbers & my_numbers

def solve(file_path):
    total_point=0
    with open(file_path) as input_file:
        for line in input_file:
            _, card_details = line.strip().split(": ")
            lucky_numbers= get_lucky_numbers(card_details)
            if len(lucky_numbers) >0:
                total_point+=math.pow(2, len(lucky_numbers)-1)
    return int(total_point)


if __name__ == "__main__":
    input_file = os.path.dirname(__file__) + "/input_day04.txt"
    print(solve(input_file))
