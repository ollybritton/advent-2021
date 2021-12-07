from utils import get_puzzle_input
from statistics import median

# Day 7 was about finding the best position for some crabs in submarines by minimising the total costs for
# all the crabs to individually move to that position. Part 1 was using the absolute difference between the
# crab's position and the target position, whereas part 2 was using a more complex scheme where the rate at
# which the cost increased would itself increase as you got further away.
# 
# Part 1 had a nice trick to it; the best value was the median of the numbers. I couldn't find any guaranteed
# nice trick for part 2, but there was a way you could find a very good starting value for a local search by
# pretending it was a parabola you could find the minimum of.
# https://adventofcode.com/2021/day/7
day = 7

def part1():
    # This is a problem of finding the median in disguise. In other words, we are asked
    #   argmin  sum( |x - a| )
    #      a
    # Where x represents each number we are given. This can be solved by finding the median.
    crab_numbers = [int(num) for num in get_puzzle_input(day).split(",")]

    min_fuel = None
    target = int(median(crab_numbers))

    fuel = sum([abs(target - x) for x in crab_numbers])
    if min_fuel == None or fuel < min_fuel:
        min_fuel = fuel

    return min_fuel

# calculate_triangle_cost calculates the cost/fuel as described in part 2 of the problem.
# Since 1 + 2 + 3 + 4 + ... n = n(n+1)/2 are the "triangle numbers" for positive integers n. 
def calculate_triangle_cost(crab_numbers, target):
    fuel = 0

    for num in crab_numbers:
        fuel += int(0.5 * abs(target - num) * (abs(target - num) + 1))

    return fuel

def part2():
    # We could now write the problem as:
    #   argmin sum( 0.5 * (|x - a|) * (|x - a| - 1) )
    #     a
    # As the sum of 1 + 2 + 3 + ... n = 0.5*n(n+1)
    #
    # You can get a pretty good approximation of this by considering only the (x-a)^2 part, which will be a
    # quadratic you can find the stationary point of using differentiation. This turns out to be the mean of the
    # numbers with some maths.
    #
    # In my puzzle input, using the rounded mean turned out to be the exact target for the valid solution. I'm not
    # sure if this holds in general though, so I wrote some local search code to make sure it hones in on the actual
    # solution.
    crab_numbers = [int(num) for num in get_puzzle_input(day).split(",")]
    mean = int(sum(crab_numbers)/len(crab_numbers))

    min_fuel = calculate_triangle_cost(crab_numbers, mean)
    target = mean
    slope = 0

    while True:
        fuel = calculate_triangle_cost(crab_numbers, target)
        fuel_up = calculate_triangle_cost(crab_numbers, target+1)
        
        if fuel > fuel_up and slope == 1:
            return fuel_up
        elif fuel < fuel_up and slope == -1:
            return fuel
        
        if fuel > fuel_up:
            # We're on a downward slope to the solution, so we need to move in the positive direction to reach the
            # solution.
            target += 1
            slope = -1
        elif fuel < fuel_up:
            # We're on an slope where moving in the positive direction will take us further away. Therefore we need to 
            # move in the negative direction to reach the solution.
            target -= 1
            slope = 1

    return min_fuel


answers = [
    [part1, 343441],
    [part2, 98925151],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())