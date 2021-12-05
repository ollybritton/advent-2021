import time

import day1
import day2
import day3
import day4
import day5

# answers are a list of [[func, official], [func, official]]
def verify(day, answers):
    now = time.time()

    for i, pair in enumerate(answers):
        got = pair[0]()
        expected = pair[1]
        print(f"Day {day}.{i+1}: got {got}, expected {expected} {'✅' if got == expected else '❌'}")

    total_ms = round((time.time() - now)*10000)/10
    print(f"Time taken: {total_ms}ms")
    print("")

    return total_ms

if __name__ == "__main__":
    total_ms = 0

    total_ms += verify(1, day1.answers)
    total_ms += verify(2, day2.answers)
    total_ms += verify(3, day3.answers)
    total_ms += verify(4, day4.answers)
    total_ms += verify(5, day5.answers)

    print(f"Took a total of {round(total_ms*100)/100}ms")