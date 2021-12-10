from utils import parse_puzzle_input

# Day 10 was about working out whether a string of brackets was valid or not, e.g. "({})" vs "({)}".
# https://adventofcode.com/2021/day/10
day = 10

corresponding = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

opening = {
    "(": True,
    "[": True,
    "{": True,
    "<": True,
    ")": False,
    "]": False,
    "}": False,
    ">": False,
}

def find_first_illegal(line):
    last = []

    for char in line:
        if opening[char]:
            last.append(char)
        else:
            if char != corresponding[last.pop()]:
                return char
        
def part1():
    mistakes = [char for char in parse_puzzle_input(day, "\n", find_first_illegal) if char != None]
    
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    return sum([points[char] for char in mistakes])

def autocomplete(line):
    last = []

    for char in line:
        if opening[char]:
            last.append(char)
        else:
            if char != corresponding[last.pop()]:
                return None

    return [corresponding[char] for char in last[::-1]]

def part2():
    completions = [c for c in parse_puzzle_input(day, "\n", autocomplete) if c != None]
    
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    scores = []

    for completion in completions:
        score = 0

        for char in completion:
            score *= 5
            score += points[char]
            
        scores.append(score)

    scores.sort()

    return scores[(len(scores))//2]

answers = [
    [part1, 271245],
    [part2, 1685293086],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())