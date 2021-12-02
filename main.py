import time

import day1
import day2

# answers are a list of [[func, official], [func, official]]
def verify(day, answers):
    now = time.time()

    for i, pair in enumerate(answers):
        got = pair[0]()
        expected = pair[1]
        print(f"Day {day}.{i+1}: got {got}, expected {expected} {'✅' if got == expected else '❌'}")

    print(f"Time taken: {round((time.time() - now)*10000)/10}ms")

if __name__ == "__main__":
    verify(1, day1.answers)
    verify(2, day2.answers)