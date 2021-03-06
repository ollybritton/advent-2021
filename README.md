# `advent-2021`
These are my Python solutions for the Advent of Code event in 2021. The goal is to write code that could be used for any input data and to be able to solve all the puzzles in less than one second total.

|Day|Name|Brief Explanation|Solution|
|-|-|-|-|
|Day 01|[Sonar Sweep](https://adventofcode.com/2021/day/1)|How many times does this sequence of numbers go up?|[`day01.py`](./day01.py)|
|Day 02|[Dive!](https://adventofcode.com/2021/day/2)|Can you keep track of a ship given the movements it makes?|[`day02.py`](./day02.py)|
|Day 03|[Binary Diagnostic](https://adventofcode.com/2021/day/3)|Can you decode this strange string of binary numbers?|[`day03.py`](./day03.py)|
|Day 04|[Giant Squid](https://adventofcode.com/2021/day/4)|Which bingo boards are the best and worst?|[`day04.py`](./day04.py)|
|Day 05|[Hydrothermal Venture](https://adventofcode.com/2021/day/5)|Where do these lines overlap?|[`day05.py`](./day05.py)|
|Day 06|[Lanternfish](https://adventofcode.com/2021/day/6)|Can you model this exponentially-growing population of fish?|[`day06.py`](./day06.py)|
|Day 07|[The Treachery of Whales](https://adventofcode.com/2021/day/7)|What's the best position for all these crabs to individually move to?|[`day07.py`](./day07.py)|
|Day 08|[Seven Segment Search](https://adventofcode.com/2021/day/8)|Can you decode this mixed up seven segment display?|[`day08.py`](./day08.py)|
|Day 09|[Smoke Basin](https://adventofcode.com/2021/day/9)|Can you find which parts of a cave system flow down to which local minimum?|[`day09.py`](./day09.py)|
|Day 10|[Syntax Scoring](https://adventofcode.com/2021/day/10)|Which string of brackets of valid?|[`day10.py`](./day10.py)|
|Day 11|[Dumbo Octopus](https://adventofcode.com/2021/day/11)|Can you model these flashing octopuses?|[`day11.py`](./day11.py)|

To try solve all problems, run:

```py
python3 main.py
```

To run one day individually, run:

```py
python3 dayN.py
```

## Layout
The input data for each day lives in [`data/inputX.txt`](./data) where `X` is the day number. The functions in [`utils.py`](./utils.py) provide convience functions for looking up and parsing the input data.

Each `dayN.py` file defines two functions `part1()` and `part2` along with a global `answers` variable which is an array that looks like

```
answers = [
    [part1, 123],
    [part2, 456],
]
```

This is then imported into [`main.py`](main.py) where the two functions are run, timed and compared against what's expected. [`day_template.py`](day_template.py) is just a template for copying and pasting each day all the scaffolding.