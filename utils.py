# puzzle_input returns the input for a particular puzzle.
def puzzle_input(day, part=0):
    path = f"data/input{day}.txt" if part == 0 else f"data/input{day}-{part}.txt"
    
    with open(path, "r") as f:
        return f.read().strip("\n")

# parse_puzzle_input returns the input for a particular puzzle, after it has been split into chunks
# and the parser applied to each.
def parse_puzzle_input(day, part=0, sep="", parser=None):
    data = puzzle_input(day, part)

    if sep != "":
        data = data.split(sep)

        if parser != None:
            data = [parser(chunk) for chunk in data]

        return data

    elif parser != None:
        return parser(data)
    else:
        return data        