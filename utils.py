# get_puzzle_input returns the input for a particular puzzle.
def get_puzzle_input(day):
    path = f"data/input{day}.txt"
    
    with open(path, "r") as f:
        return f.read().strip("\n")

# parse_puzzle_input returns the input for a particular puzzle, after it has been split into chunks
# and the parser applied to each.
def parse_puzzle_input(day, sep="", parser=None):
    data = get_puzzle_input(day)

    if sep != "":
        data = data.split(sep)

        if parser != None:
            data = [parser(chunk) for chunk in data]

        return data

    elif parser != None:
        return parser(data)
    else:
        return data        