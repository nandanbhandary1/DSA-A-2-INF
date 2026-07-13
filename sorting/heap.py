import heapq


def heap_sort(arr):
    heapq.heapify(arr)  # Convert it into heap structure
    n = len(arr)
    ans = [0] * n
    for i in range(n):
        minn = heapq.heappop(arr)
        ans[i] = minn
    return ans


print(heap_sort([1, 9, 63, 4, 886, 35, 10, 74]))

