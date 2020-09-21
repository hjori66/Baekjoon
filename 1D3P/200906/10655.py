import sys

pair_list = list()
N = int(sys.stdin.readline())
for _ in range(N):
    pair_list.append(tuple(map(int, sys.stdin.readline().split())))

honest_path = 0
reduced_distance = 0
for i, pair in enumerate(pair_list):
    if i > 0:
        x1, y1 = pair_list[i-1]
        x2, y2 = pair
        honest_path += int(abs(x1-x2)) + int(abs(y1-y2))

        if i < len(pair_list) - 1:
            x3, y3 = pair_list[i+1]
            path1 = int(abs(x1-x2)) + int(abs(y1-y2))
            path2 = int(abs(x2-x3)) + int(abs(y2-y3))
            short_path = int(abs(x1-x3)) + int(abs(y1-y3))
            reduced_distance = max(reduced_distance, path1 + path2 - short_path)
print(honest_path - reduced_distance)
