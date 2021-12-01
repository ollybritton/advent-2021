from utils import parse_puzzle_input

def part1():
    nums = parse_puzzle_input(1, 1, "\n", int)
    count = 0

    for i, num in enumerate(nums):
        if i != 0 and nums[i-1] < num:
            count += 1

    return count

def part2():
    nums = parse_puzzle_input(1, 1, "\n", int)
    count = 0

    for i in range(len(nums)):
        if i > 3 and nums[i-3] < nums[i]:
            count += 1

    return count

answers = [
    [part1, 1139],
    [part2, 1103],
]

if __name__ == "__main__":
    print("Part 1:", part1()) # 1139
    print("Part 2:", part2()) # 1103