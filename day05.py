from utils import parse_puzzle_input

# Day 5 was about finding the amount of times that a point was passed through by at least 2 lines.
# https://adventofcode.com/2021/day/5
# 
# The approach I take here is to work out all the points that the lines go through, store them in a data
# structure that counts the number of times a point has been added, and then work out the number of ones
# that had been added twice.
# 
# This isn't super fast -- I'm pretty sure that there would be an algorithm that found just the points of
# intersection instead of working out all of them.
day = 5

# Point lets us conviently refer to the first and second part of the coordinate as .x and .y
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

# Intersections provides a data structure for counting the amount of times a coordinate has been added
# Instead of storing an 1000 x 1000 multi-dimensional array of coordinates, most which would be 0, we
# instead only store the ones that exist.
class Intersections():
    def __init__(self):
        self.coordinates = {}

    def add_point(self, x, y):
        if self.coordinates.get(x) == None:
            self.coordinates[x] = {y: 1}
        else:
            if self.coordinates[x].get(y) == None:
                self.coordinates[x][y] = 1
            else:
                self.coordinates[x][y] += 1

    def lookup(self, x, y):
        if self.coordinates.get(x) == None:
            return 0
        else:
            if self.coordinates[x].get(y) == None:
                return 0
            else:
                return self.coordinates[x][y]

    def above_threshold(self, threshold):
        total = 0
        
        for ys in self.coordinates.values():
            for count in ys.values():
                if count >= threshold:
                    total += 1
                    
        return total


# parse_line turns one line of the input into an array of points.
# For example: parse_line("617,237 -> 951,237") -> Point()
def parse_line(line):
    pairs = line.split(" -> ")
    
    start = Point(*[int(num) for num in pairs[0].split(",")])
    end = Point(*[int(num) for num in pairs[1].split(",")])

    return [start, end]

# point_range forms an inclusive range that either goes up or down.
# For example: point_range(1,5) -> [1,2,3,4,5]
#              point_range(5,1) -> [5,4,3,2,1]
def point_range(a, b):
    if a > b:
        return range(a, b-1, -1)
    else:
        return range(a, b+1)

def part1():
    # [[Point(x1, y1), Point(x2, y2)], ...]
    point_pairs = parse_puzzle_input(day, "\n", parse_line)
    counts = Intersections()

    for pair in point_pairs:
        pair = list(pair)

        if pair[0].x == pair[1].x: # Line of the form x = n
            x = pair[0].x
            
            for y in point_range(pair[0].y, pair[1].y):
                counts.add_point(x, y)

        elif pair[0].y == pair[1].y: # Line of the form y = n
            y = pair[0].y

            for x in point_range(pair[0].x, pair[1].x):
                counts.add_point(x, y)

    return counts.above_threshold(2)

def part2():
    point_pairs = parse_puzzle_input(day, "\n", parse_line)
    counts = Intersections()

    for pair in point_pairs:
        pair = list(pair)

        if pair[0].x == pair[1].x: # Line of the form x = n
            x = pair[0].x
            
            for y in point_range(pair[0].y, pair[1].y):
                counts.add_point(x, y)

        elif pair[0].y == pair[1].y: # Line of the form y = n
            y = pair[0].y

            for x in point_range(pair[0].x, pair[1].x):
                counts.add_point(x, y)

        else: # Line of the form y = (+/-)x + c
            pair = sorted(pair, key=lambda x: x.x)

            c = 0
            m = 0
            
            if pair[0].y < pair[1].y:
                # Slope increasing, y = x + c
                # "c" can be calculated from the formula y - y1 = m(x - x1)
                m = 1
                c = pair[0].y - pair[0].x

            else:
                # Slope decreasing, y = -x + c 
                m = -1
                c = pair[0].y + pair[0].x

            xs = point_range(pair[0].x, pair[1].x)

            for x in xs:
                y = m*x + c
                counts.add_point(x, y)


    return counts.above_threshold(2)

answers = [
    [part1, 5576],
    [part2, 18144],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())