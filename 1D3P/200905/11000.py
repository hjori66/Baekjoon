import sys, heapq

pair_list = list()
pair_heap = list()
N = int(sys.stdin.readline())
for _ in range(N):
    pair_list.append(tuple(map(int, sys.stdin.readline().split())))
pair_list.sort()

num_class = 0

for i, pair in enumerate(pair_list):
    left, right = pair
    heapq.heappush(pair_heap, (right, left))
    if i == 0:
        num_class += 1
    if i > 0:
        heap_right, heap_left = pair_heap[0]
        if left < heap_right:
            num_class += 1
        else:
            heapq.heappop(pair_heap)

print(num_class)
