from utils import parse_puzzle_input

# Day 8 was about working out what a faulty 7-segment display was actually doing. This was the first one that took me more
# than a day to figure it out. I didn't read the description well enough and thought that they only gave you 6 examples instead
# of 9, where each number of 6 corresponded to only one number that was that length.
# https://adventofcode.com/2021/day/8
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

# set_to_sorted_string converts a set containing characters to a sorted string.
def set_to_sorted_string(s):
    return "".join(sorted(list(s)))


def part2():
    data = parse_puzzle_input(day, "\n", parse_line)
    
    total = 0

    for message in data:
        length_map = {} # maps signal lengths to the signals that contain them.
        true_map = {} # maps alphabetically sorted signals to the number they represent.
        
        for signal in message[0]:
            length = len(signal)
            
            if length_map.get(length) == None:
                length_map[length] = [set(signal)]
            else:
                length_map[length].append(set(signal))

        # Take care of the uniquely numbered ones.
        true_map[set_to_sorted_string(length_map[2][0])] = 1
        true_map[set_to_sorted_string(length_map[4][0])] = 4
        true_map[set_to_sorted_string(length_map[3][0])] = 7
        true_map[set_to_sorted_string(length_map[7][0])] = 8
    
        # Look at the coding for number 1 (unique length 1) and for number 7 (unique length 3).
        # The coding for the "a" segment will be the one in 7 that isn't in 1.
        true_a = length_map[3][0].difference(length_map[2][0])
        
        values_bd = length_map[2][0].symmetric_difference(length_map[4][0])
        values_eg = length_map[4][0].symmetric_difference(length_map[7][0]) - true_a

        for number in length_map[5]:
            if len(number.intersection(values_eg)) == 2: # The number 2 is the only number containing both E and G of length 5.
                true_map[set_to_sorted_string(number)] = 2
            elif len(number.intersection(values_bd)) == 2: # The number 5 is the only number containing both B and D of length 5.
                true_map[set_to_sorted_string(number)] = 5
            else:
                true_map[set_to_sorted_string(number)] = 3

        for number in length_map[6]:
            if len(number.intersection(values_eg)) == 2: # Only number 6 and number 0 have both an E and a G.
                if len(number.intersection(values_bd)) == 2: # Only number 6 has both B and D and is of length 5.
                    true_map[set_to_sorted_string(number)] = 6
                else: # Must be a zero.
                    true_map[set_to_sorted_string(number)] = 0

            else: # Must be number 9.
                true_map[set_to_sorted_string(number)] = 9 
                
        number = ""

        for code in message[1]:
            number += str(true_map["".join(sorted(code))])

        total += int(number)

    return total

answers = [
    [part1, 473],
    [part2, 1097568],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())