import sys
import math

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

# arr = [5,3,2,5,7]
# print(sorted(arr, reverse=True))
# print(arr.sort())


# arr = [-1, -6, 7, -3, -99]
# print(sorted(arr, key=lambda x: abs(x)))


# fruits = ["apple", "pineapple", "kiwi"]
# print(sorted(fruits, reverse=True, key=len))


# nums = [1,2,3,4, -75]
# print(max(nums, key=lambda x:abs(x)))


# arr = [1,2,3,4]
# print(sum(arr, start=2))
# print(math.prod(arr))

# print(list(reversed(arr)))

# from collections import deque

# dp = deque([1,2,3])
# dp.append(5)
# dp.appendleft(7)
# ele = dp.pop()
# dp.extend([5,6,7])
# print(dp)
# print(ele)

# from collections import Counter

# c1 = Counter([11, 23, 4, 5, 6, 3, 2, 12, 45, 6, 7, 8, 6, 5, 4, 2, 2])

# print(c1[6])
# print(arr.most_common(7))
# print(list(arr.elements()))

# c2 = Counter([3,3,1,4,5])

# c3 = c1 - c2
# c3 = c1 + c2
# c3 = c1 & c2
# c3 = c1 | c2
# print(list(c3.elements()))

# from collections import defaultdict

# dd = defaultdict(int)

# dd["name"] = "nandan"
# dd["age"] = 23
# dd["list"] = [1, 2, 3]

# print(dd["list"])
# print(dd)

# print(dd["nandan"])

# from collections import OrderedDict

# d = OrderedDict([(1, "nandan"), (2, "Namru")])

# print(d[1])


# l1 = [1, 2, 3]
# l2 = [2, 1, 3]
# print(l1 == l2)


# q = (1, (1,2,3))

# a, (b,c,d) = q

# print(a,b,c,d)

# from collections import namedtuple

# point = namedtuple("nandan", ["first", "second"])
# val = point(7,9)
# print(val)
# print(val.first)


# test = namedtuple("ba", 'a')
# val = test(4)
# print(val)

# second = namedtuple("second", ['first', 'second'])
# val = second(6,9)
# first = namedtuple("first", ['first', 'second'])
# ans = first(2, val)
# print(ans.second.second)

