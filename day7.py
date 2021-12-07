from utils import get_puzzle_input

# Day 7 was about ...
# https://adventofcode.com/2021/day/7
# 
day = 7

def part1():
    crab_numbers = [int(num) for num in get_puzzle_input(day).split(",")]
    # Optimal value would be the x-coordinate of the stationary point of
    # y = sum(abs(num - x))
    
    target = 2

    count_lt = sum([1 if x < target else 0 for x in crab_numbers])
    count_gt = sum([1 if x >= target else 0 for x in crab_numbers])

    print(count_lt, count_gt)

    fuel = sum([x - target for x in crab_numbers if x > target]) + sum([target - x for x in crab_numbers if x <= target])
    return fuel

def part2():
    # parse_puzzle_input(day, "\n", int)
    pass

answers = [
    # [part1, 101],
    # [part2, 101],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    # print("Part 2:", part2())