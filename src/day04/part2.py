import os
import math


def get_match_count(card):
    winning_numbers, my_numbers = [set(x.split()) for x in card.split(" | ")]
    # set intersection
    return len(winning_numbers & my_numbers)


def solve(file_path):
    total_points = 0
    card_matches = []
    with open(file_path) as input_file:
        for line in input_file:
            card_details = line.strip().split(": ")[1]
            card_matches.append(get_match_count(card_details))
    card_count = [1] * len(card_matches)
    for i, matches in enumerate(card_matches):
        total_points += card_count[i]
        j = matches
        while j > 0:
            card_count[i + j] += card_count[i]
            j-=1
    return total_points


if __name__ == "__main__":
    input_file = os.path.dirname(__file__) + "/input_day04.txt"
    print(solve(input_file))
