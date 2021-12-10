from utils import parse_puzzle_input

# Day 2 was about keeping track of a ship given movements it makes.
# https://adventofcode.com/2021/day/2
day = 2

def parse_line(line):
    line = line.split(" ")
    return line[0], int(line[1])

def part1():
    data = parse_puzzle_input(day, "\n", parse_line)
    
    horizontal = 0
    depth = 0

    for direction, magnitude in data:
        if direction == "forward":
            horizontal += magnitude
        elif direction == "up":
            depth -= magnitude
        else:
            depth += magnitude

    return horizontal * depth

def part2():
    data = parse_puzzle_input(day, "\n", parse_line)
    
    horizontal = 0
    depth = 0
    aim = 0

    for direction, magnitude in data:
        if direction == "forward":
            horizontal += magnitude
            depth += aim * magnitude
        elif direction == "up":
            aim -= magnitude
        elif direction == "down":
            aim += magnitude


    return horizontal * depth

answers = [
    [part1, 1690020],
    [part2, 1408487760],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())