import sys
import bisect

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


arr = [1,2,3,4,5,6,7]

print(bisect.bisect_left(arr, 5))

bisect.insort(arr, 5)

print(arr)