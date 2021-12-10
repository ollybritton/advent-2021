from utils import parse_puzzle_input
from functools import lru_cache


# Day 9 was about finding the basins for an underground cave system, which are collections of points that all
# flow down to some local minimum. The second part was fun, I tackled it recursively by finding the "destination"
# a point belonged to by looking at the destination for its neighbour with the smallest value.
# 
# https://adventofcode.com/2021/day/9
day = 9

# Grid is a convenience class for 
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

    # Returns the item at the location if it exists, otherwise none.
    def get_if_exists(self, x, y):
        if not self.valid_index(x, y):
            return None
        else:
            return self.rows[y][x]

    def get_adjacent(self, x, y):
        return list(filter(lambda x: x is not None, [
            self.get_if_exists(x, y-1),
            self.get_if_exists(x-1, y),
            self.get_if_exists(x+1, y),
            self.get_if_exists(x, y+1),
        ]))
        
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

        return indicies


def part1():
    heightmap = parse_puzzle_input(day, "\n", lambda line: [int(digit) for digit in line])
    heightmap = Grid(heightmap)

    risk = 0

    for x in range(heightmap.width()):
        for y in range(heightmap.height()):
            num = heightmap.get(x, y)
            adjacent = heightmap.get_adjacent(x, y)

            if all([num < x for x in adjacent]):
                risk += 1 + num 

    return risk


def part2():
    heightmap = Grid(parse_puzzle_input(day, "\n", lambda line: [int(digit) for digit in line]))
    basins = {} # basin[(x, y)] -> count

    for x in range(heightmap.width()):
        for y in range(heightmap.height()):
            num = heightmap.get(x, y)
            adjacent = heightmap.get_adjacent(x, y)

            # i.e. if every neighbour is less than this one, count this as a basin.
            if all([num < x for x in adjacent]):
                basins[(x, y)] = 0 

    # Defining this as a closure lets us use "basins" as a variable. If we defined this out of the scope of this
    # function, then the lru_cache wouldn't work as basins (a dict) is an unhashable type. Adding this cuts the runtime
    # in half!
    #
    # We could also do this iteratively, by keeping some sort of "frontier" and "visited" variable. Using lru_cache
    # abstracts a lot of this away from us and means we don't have to deal with any sort of cache ourselves.
    @lru_cache(maxsize=None)
    def find_basin(heightmap, x, y):
        if basins.get((x, y)) != None:
            return (x, y)

        adj = heightmap.get_adjacent_indicies(x, y)
        
        minimum = min(adj, key=lambda x: heightmap.get(*x))
        return find_basin(heightmap, *minimum)

    for x in range(heightmap.width()):
        for y in range(heightmap.height()):
            num = heightmap.get(x, y)

            if num == 9:
                continue
            
            basinX, basinY = find_basin(heightmap, x, y)

            basins[(basinX, basinY)] += 1
            continue

    
    scores = sorted(basins.values())
    overall_score = 1

    for i in range(len(scores)-3, len(scores)):
        overall_score *= scores[i]

    return overall_score

answers = [
    [part1, 475],
    [part2, 1092012],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())