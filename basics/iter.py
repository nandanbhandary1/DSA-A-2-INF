import sys
import itertools

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


arr = [1, 2, 3]

print(list(itertools.combinations(arr, 2)))

print(list(itertools.combinations_with_replacement(arr, 2)))

print(list(itertools.permutations(arr)))

""" 
CONVERT TO LIST USE LIST COMPREHENSION
"""
print([list(item) for item in itertools.permutations(arr)])


a1 = [1, 2]
a2 = [3, 4]

print(list(itertools.product(a1, a2)))
print([list(item) for item in itertools.product(a1, a2)])

print(list(itertools.repeat(5, 5)))

print(list(itertools.chain([1, 2], [3, 5], (7, 8), {9, 10})))

ar = [10, 2, 3, 4]
print(list(itertools.accumulate(ar)))

# sum = []
# for i in range(len(ar)):
#     if not sum:
#         sum.append(ar[i])
#     else:
#         sum.append(ar[i] + sum[i-1])
# print(sum)


print(list(itertools.accumulate(ar, lambda x, y: x * y)))
