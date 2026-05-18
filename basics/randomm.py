import sys
import random

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

arr = [1,2,3,4,5]

print(random.random())
print(random.randint(1, 10))
print(random.uniform(1,10))
print(random.randrange(0, 100, 2))
print(random.choice((1,2,3,4,5)))
print(random.sample([1,2,3,4], 2))
random.shuffle(arr)
print(arr)

num = 6.3556656654
print(round(num, 2))
print(f"{num:.3f}")