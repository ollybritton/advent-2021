from utils import parse_puzzle_input

# Day 1 was about counting the number of times the numbers in a list increases rather than decreases.
# https://adventofcode.com/2021/day/1
day = 1

def part1():
    nums = parse_puzzle_input(day, "\n", int)
    count = 0

    for i, num in enumerate(nums):
        if i != 0 and nums[i-1] < num:
            count += 1

    return count

def part2():
    nums = parse_puzzle_input(day,"\n", int)
    count = 0

    for i in range(len(nums)):
        # If we have
        #   nums[i-3] + nums[i-2] + nums[i-1] < nums[i-2] + nums[i-1] + nums[i]
        # We can subtract (nums[i-2] + nums[i-1]) from both sides of the inequality without changing
        # if it is true, so we only need to compare two.
        if i > 3 and nums[i-3] < nums[i]:
            count += 1

    return count

answers = [
    [part1, 1139],
    [part2, 1103],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())