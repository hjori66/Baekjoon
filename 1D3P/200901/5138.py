import sys

K = int(sys.stdin.readline())
for i in range(K):
    V, E = map(int, sys.stdin.readline().split())

    leaf_dist = [-1] * (V+1)
    sum = 0
    for j in range(E):
        start, end, dist = map(int, sys.stdin.readline().split())
        sum += dist*2
        if start > 1 and leaf_dist[start] < 0:
            leaf_dist[start] = dist
        else:
            leaf_dist[start] = 0

        if end > 1 and leaf_dist[end] < 0:
            leaf_dist[end] = dist
        else:
            leaf_dist[end] = 0

    print("Data Set {}:".format(i+1))
    print(sum - 2*max(leaf_dist))
    print()
