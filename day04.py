from utils import get_puzzle_input

# Day 4 was about finding the best and the worst bingo boards.
# https://adventofcode.com/2021/day/4
#
# The approach I take here isn't anything fancy. The Board class represents a bingo board
# which can be marked and checked for solutions. For part 1, it finds the first winning board.
# For part 2, it plays all the boards until it gets down to one last one.
day = 4

# Board represents a Bingo board. For example, 
#   99 49 50
#   48 59 76
#   11 53 51
# Could be constructed using the array [[99, 49, 50], [48, 59, 76], [11, 53, 51]]
class Board():
    def __init__(self, rows):
        self.rows = rows
        self.marked = {}
        self.size = len(rows[0])
        self.cols = [[] for _ in range(self.size)]

        for row in rows:
            for i, num in enumerate(row):
                self.cols[i].append(num)
                self.marked[num] = False

    def row(self, index):
        return self.rows[index]

    def col(self, index):
        return self.cols[index]

    def mark(self, num):
        self.marked[num] = True

    def num_marked(self, nums):
        count = 0
        for num in nums:
            if self.marked[num]:
                count += 1

        return count

    def has_won(self, diag=False):
        for i in range(self.size):
            if self.num_marked(self.row(i)) == self.size:
                return True
            
            if self.num_marked(self.col(i)) == self.size:
                return True

        return False

    def score(self, most_recent):
        total = 0

        for row in self.rows:
            for num in row:
                if not self.marked[num]:
                    total += num

        return total * most_recent

# parse_board assumes that the numbers are between 0-100 and are arranged in a 5x5 grid.
def parse_board(string):
    unparsed_rows = string.split("\n")
    rows = []
    
    for row in unparsed_rows:
        # While it would be possible to put this into a loop, since the board always follows
        # the same format then this might be marginally faster.
        rows.append([
            int(row[0:2]),
            int(row[3:5]),
            int(row[6:8]),
            int(row[9:11]),
            int(row[12:14]),
        ])

    return Board(rows)

def part1():
    puzzle_input = get_puzzle_input(day)

    draw_nums = [int(x) for x in puzzle_input.split("\n")[0].split(",")]
    boards = [parse_board(x) for x in puzzle_input.split("\n\n")[1:]]
    
    for num in draw_nums:
        for board in boards:
            board.mark(num)

            if board.has_won():
                return board.score(num)

def part2():
    puzzle_input = get_puzzle_input(day)

    draw_nums = [int(x) for x in puzzle_input.split("\n")[0].split(",")]
    boards = [parse_board(x) for x in puzzle_input.split("\n\n")[1:]]

    last_score = 0
    
    for num in draw_nums:
        # It's neccessary here copy the list here so that we can safely remove boards if they have won. If we didn't do this,
        # the boards list would change as we go through the list whereas we want to do it in "sweeps".
        for board in boards.copy():
            board.mark(num)

            if board.has_won():
                boards.remove(board)
                last_score = board.score(num)

    return last_score

answers = [
    [part1, 33462],
    [part2, 30070],
]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())