from utils import get_puzzle_input

# Day 6 was about modelling a population of lanternfish that grew exponentially. I thought it would
# be better to use a dictionary mapping the "timers" to the numbers of fish with that timer since storing
# every single one in an array would mean it could take a long time.
# 
# This turned out to be the right approach! Part two wanted it after 256 days instead of 18 days which
# would've been slow/impossible due to the exponential growth. You would've needed an array 6.3TB big.
# https://adventofcode.com/2021/day/6
day = 6

# add_or_set will set the value of the key in the dictionary to the number if it doesn't exist,
# or it will add it.
def add_or_set(d, key, val):
    if d.get(key) == None:
        d[key] = val
    else:
        d[key] += val

def model_fish(population, days):
    timers = {} # fish timer -> fish number

    for number in population:
        if timers.get(number) == None:
            timers[number] = 1
        else:
            timers[number] += 1

    for _ in range(days):
        new_timers = {}

        for timer_value in timers.keys():
            fish_number = timers[timer_value]
            
            if timer_value == 0:
                add_or_set(new_timers, 8, fish_number)  
                add_or_set(new_timers, 6, fish_number)

            else:
                add_or_set(new_timers, timer_value-1, fish_number)

        timers = new_timers

    total = 0

    for fish_number in timers.values():
        total += fish_number

    return total

def part1():
    population = [int(x) for x in get_puzzle_input(day).split(",")]
    return model_fish(population, 18)


def part2():
    population = [int(x) for x in get_puzzle_input(day).split(",")]
    return model_fish(population, 256)

answers = [
    [part1, 1861],
    [part2, 1743335992042],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())