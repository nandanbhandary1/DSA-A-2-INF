import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

arr = [1, 5, 2, 8, 9]

arr.append(7)

print(arr)

arr.extend([0,12])
print(arr)

s = {7,8,-1,0}
print(s)
s.pop()
s.pop()
print(s)