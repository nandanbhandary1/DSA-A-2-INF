import sys
import heapq

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

val = []

heapq.heappush(val, 1)
heapq.heappush(val, 4)
heapq.heappush(val, 3)
heapq.heappush(val, 0)
heapq.heappush(val, 7)

heapq.heappop(val)

heapq.heappushpop(val, 8)

heapq.heapreplace(val, 1)

print(val[0])

print(heapq.nlargest(2, [3, 5, 6, 12]))

print(val)


# arr = [7,8,2,1,-16,6]

# val = []
# for items in arr:
#     heapq.heappush(val, items)

# print(val)

"""
MIN HEAP
"""
# heapq.heapify(arr)
# print(arr)


"""
MAX HEAP
"""
max_heapp = [7, 8, 2, 1, -16, 6]

ans = []

for item in max_heapp:
    heapq.heappush(ans, -1 * item)

max_heapp = [-item for item in ans]

print(max_heapp)

heapq.heapify(-1 * max_heapp)
max_heapp = [-item for item in ans]

print(max_heapp)


""" 
MAX HEAP
"""
# Original array
arr = [7, 8, 2, 1, -16, 6]

# Convert into max heap
max_heap = [-item for item in arr] # NEGATE THE ELEMENTS

heapq.heapify(max_heap) # CONVERT THAT TO A MIN HEAP

max_heapp = [-item for item in max_heap] # NEAGATE AGAIN AND DONE

print(max_heapp)

