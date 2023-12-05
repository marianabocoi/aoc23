import os

def expand_seeds_ranges(seeds_ranges):
    seeds = []
    for i in range(0,len(seeds_ranges),2):
        seeds += list(range(seeds_ranges[i],seeds_ranges[i]+seeds_ranges[i+1]))
    return seeds

def get_mapping(file_path):
    seeds = []
    mapping = {}
    destinations = {}
    source = ""
    destination = ""
    with open(file_path) as input_file:
        seeds_str = input_file.readline().strip().split(":")[1].split()
        seeds_ranges = [int(x) for x in seeds_str]
        seeds = expand_seeds_ranges(seeds_ranges)
        for line in input_file:
            if "-to-" in line:
                transformation = line.strip().split()[0]
                source, destination = transformation.split("-to-")
                mapping[source] = {}
                mapping[source][destination] = []
                destinations[destination] = source
            else:
                numbers = line.strip().split()
                if len(numbers) == 3:
                    destination_start, source_start, length = [int(x) for x in numbers]
                    mapping[source][destination].append(
                        {
                            "source_start": source_start,
                            "source_end": source_start + length - 1,
                            "destination_start": destination_start,
                            "destination_end": destination_start + length - 1,
                            "conversion": destination_start - source_start,
                            "length": length,
                        }
                    )
    return seeds, mapping, destinations


def convert(id, mapping):
    for m in mapping:
        if id >= m["source_start"] and id <= m["source_end"]:
            return id + m["conversion"]
    return id


def convert_list(ids, source, destination, mapping):
    return [convert(x, mapping[source][destination]) for x in ids]


def find_path(start, end, destinations):
    path = {}
    hop_over = end
    while hop_over != start:
        path[destinations[hop_over]] = hop_over
        hop_over = destinations[hop_over]
    return path


def convert_list_recursive(file_path):
    start = "seed"
    end = "location"
    seeds, mapping, destinations = get_mapping(file_path)
    path = find_path(start, end, destinations)
    values = seeds
    hop_over = start
    # print("init> ",start, hop_over, end, values)
    while hop_over != end:
        values = convert_list(values, hop_over, path[hop_over], mapping)
        #    print("step> ",hop_over, path[hop_over], end, values)
        hop_over = path[hop_over]
    return values


def solve(file_path):
    return min(convert_list_recursive(file_path))


if __name__ == "__main__":
    input_file = os.path.dirname(__file__) + "/input_day05.txt"
    print(solve(input_file))
