
import day1

# answers are a list of [[func, official], [func, official]]
def verify(day, answers):
    for i, pair in enumerate(answers):
        got = pair[0]()
        expected = pair[1]
        print(f"Day {day}.{i+1}: got {got}, expected {expected} {'✅' if got == expected else '❌'}")

if __name__ == "__main__":
    verify(1, day1.answers)