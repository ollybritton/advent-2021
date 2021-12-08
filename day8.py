from utils import parse_puzzle_input

# Day 8 was about ...
# https://adventofcode.com/2021/day/8
# 
day = 8

def parse_line(line):
    splitted = line.split(" | ")
    return (splitted[0].split(" "), splitted[1].split(" "))

def part1():
    data = parse_puzzle_input(day, "\n", parse_line)
    total = 0

    for message in data:
        output = message[1]

        count = 0
        
        for digit in output:
            if len(digit) == 2 \
               or len(digit) == 4 \
               or len(digit) == 3 \
               or len(digit) == 7:
                count += 1

        total += count

    return total

# add_or_set will set the value of the key in the dictionary to the number if it doesn't exist,
# or it will add it.
def add_or_set(d, key, val):
    if d.get(key) == None:
        d[key] = val
    else:
        d[key] += val

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
# 
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg
# 
# 1, 4, 7 and 8 have unique numbers of turned on segments.
# 
# 1: 2 are turned on.
# 4: 4 are turned on.
# 7: 3 are turned on.
# 8: 7 are turned on.
#
# Can compare 1 and 7 to determine the value of "a". 
def part2():
    data = parse_puzzle_input(day, "\n", parse_line)

    for message in data:
        length_map = {}
        
        for signal in message[0]:
            length = len(signal)
            length_map[length] = set(signal)
        
            
        # Look at the coding for number 1 (unique length 1) and for number 7 (unique length 3).
        # The coding for the "a" segment will be the one in 7 that isn't in 1.
        true_a = length_map[3].difference(length_map[2])
        
        values_bd = length_map[2].symmetric_difference(length_map[4])
        values_eg = length_map[4].symmetric_difference(length_map[7]) - true_a
    
        if len(length_map[5].intersection(values_eg)) != 1:
            # The encoding for length of 5 is a 2.
            true_c = length_map[5].intersection(length_map[3]) - true_a
            true_f = length_map[2] - true_c
            # print(true_a, true_c, true_f)

        else:
            true_g = length_map[5].intersection(values_eg)

            print(true_g)


    return

answers = [
    # [part1, 101],
    # [part2, 101],
]

if __name__ == "__main__":
    # print("Part 1:", part1())
    print("Part 2:", part2())