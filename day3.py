from utils import parse_puzzle_input

day = 3

def part1():
    data = parse_puzzle_input(day, 1, "\n", lambda x: x)
    length = len(data)
    
    ones = [0] * 12

    for num in data:
        for i, digit in enumerate(list(num)):
            if digit == "1":
                ones[i] += 1

    # We don't need to keep track of zeroes in each position since the number of zeroes with be
    # length-ones.
    most_common = "".join(["1" if 2*ones[i] > length else "0" for i in range(12)])
    least_common = "".join(["1" if 2*ones[i] < length else "0" for i in range(12)])

    gamma = int(most_common, 2)
    epsilon = int(least_common, 2)

    return gamma * epsilon
    

def part2():
    data = parse_puzzle_input(day, 1, "\n", lambda x: x)

    oxygen_data = data
    co2_data = data.copy()

    current_bit_index = 0
    while len(oxygen_data) > 1 and current_bit_index <= 12:
        ones = 0
        zeroes = 0

        for num in oxygen_data:
            if num[current_bit_index] == "0":
                zeroes += 1
            elif num[current_bit_index] == "1":
                ones += 1
        


        if ones >= zeroes:
            oxygen_data = [num for num in oxygen_data if num[current_bit_index] == "1"]
        else:
            oxygen_data = [num for num in oxygen_data if num[current_bit_index] == "0"]

        current_bit_index += 1
    
    current_bit_index = 0
    while len(co2_data) > 1 and current_bit_index <= 12:
        ones = 0
        zeroes = 0

        for num in co2_data:
            if num[current_bit_index] == "0":
                zeroes += 1
            elif num[current_bit_index] == "1":
                ones += 1
        
        if ones >= zeroes:
            co2_data = [num for num in co2_data if num[current_bit_index] == "0"]
        else:
            co2_data = [num for num in co2_data if num[current_bit_index] == "1"]

        current_bit_index += 1

    co2_rating = int(co2_data[0], 2)
    oxygen_rating = int(oxygen_data[0], 2)

    return co2_rating * oxygen_rating



answers = [
    [part1, 4103154],
    [part2, 4245351],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())