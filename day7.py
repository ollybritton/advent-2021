from utils import get_puzzle_input
from statistics import median

# Day 7 was about ...
# https://adventofcode.com/2021/day/7
# 
day = 7

def part1():
    crab_numbers = [int(num) for num in get_puzzle_input(day).split(",")]

    min_fuel = None

    for target in range(min(crab_numbers), max(crab_numbers)):
        fuel = sum([abs(target - x) for x in crab_numbers])
        if min_fuel == None or fuel < min_fuel:
            min_fuel = fuel

    return min_fuel

def part2():
    crab_numbers = [int(num) for num in get_puzzle_input(day).split(",")]

    min_fuel = None

    for target in range(min(crab_numbers), max(crab_numbers)):
        fuel = sum([int(0.5*abs(target - x)*(abs(target - x)+1)) for x in crab_numbers])
        if min_fuel == None or fuel < min_fuel:
            min_fuel = fuel

    return min_fuel


answers = [
    [part1, 343441],
    [part2, 98925151],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())