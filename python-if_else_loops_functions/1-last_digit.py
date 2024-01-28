#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
positive = number
if number < 0:
    positive = number * -1
    last = positive % 10
    if last != 0:
        last = last * -1
else:
    last = positive % 10
print(f"Last digit of {number} is {last}", end="")
if last > 5:
    print(" and is greater than 5")
elif last < 6 and positive % 10 != 0:
    print(" and is less than 6 and not 0")
else:
    print(" and is 0")
