from utils import parse_puzzle_input

# Day 11 was about watching some dumbo octopuses that could flash.
# https://adventofcode.com/2021/day/10
day = 11

class Grid:
    def __init__(self, rows):
        self.rows = rows

    def width(self):
        return len(self.rows[0])
    
    def height(self):
        return len(self.rows)

    def valid_index(self, x, y):
        if y < 0 or y >= len(self.rows):
            return False
        elif x < 0 or x >= len(self.rows[0]):
            return False
        else:
            return True

    # Indexed from the top left (0,0) to the bottom right (n, n)
    def get(self, x, y):
        return self.rows[y][x]
    
    def clear(self, x, y):
        self.rows[y][x] = 0

    # Add adds a number to that position.
    def add(self, x, y, num):
        self.rows[y][x] += num

    # Returns the item at the location if it exists, otherwise none.
    def get_if_exists(self, x, y):
        if not self.valid_index(x, y):
            return None
        else:
            return self.rows[y][x]

    def get_adjacent_indicies(self, x, y):
        indicies = []

        if self.valid_index(x, y-1):
            indicies += [(x, y-1)]
        
        if self.valid_index(x-1, y):
            indicies += [(x-1, y)]
        
        if self.valid_index(x+1, y):
            indicies += [(x+1, y)]
        
        if self.valid_index(x, y+1):
            indicies += [(x, y+1)]

        if self.valid_index(x-1, y-1):
            indicies += [(x-1, y-1)]

        if self.valid_index(x+1, y-1):
            indicies += [(x+1, y-1)]

        if self.valid_index(x-1, y+1):
            indicies += [(x-1, y+1)]

        if self.valid_index(x+1, y+1):
            indicies += [(x+1, y+1)]

        return indicies

    def get_adjacent(self, x, y):
        return list(map(lambda arg: self.get(*arg), self.get_adjacent_indicies(x, y)))
        
    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.rows])

    def step(self):
        num_modified = 0

        for y, row in enumerate(self.rows):
            for x, _ in enumerate(row):
                self.add(x, y, 1)

        modified = True
        
        while modified:
            modified = False

            for y, row in enumerate(self.rows):
                for x, val in enumerate(row):
                    if val <= 9:
                        continue

                    self.clear(x, y)
                    modified = True
                    num_modified += 1

                    for adjX, adjY in self.get_adjacent_indicies(x, y):
                        if self.get(adjX, adjY) != 0:
                            self.add(adjX, adjY, 1)

        return num_modified


def part1():
    grid = Grid(parse_puzzle_input(day, "\n", lambda line: [int(x) for x in str(line)]))
    flashes = 0
    
    for _ in range(100):
        flashes += grid.step()

    return flashes

def part2():
    grid = Grid(parse_puzzle_input(day, "\n", lambda line: [int(x) for x in str(line)]))
    steps = 1

    while grid.step() != 100:
        steps += 1

    return steps

answers = [
    [part1, 1601],
    [part2, 368],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())