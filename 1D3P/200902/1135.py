import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

time_list = [-1 for _ in range(N)]
child_list = [list() for _ in range(N)]
for i, num in enumerate(num_list):
    if i > 0:
        child_list[num].append(i)


def call_time(index):
    if time_list[index] >= 0:
        return time_list[index]
    length = len(child_list[index])
    if not length:
        time_list[index] = 0
        return time_list[index]
    child_time_list = [call_time(child) for child in child_list[index]]
    child_time_list.sort()
    for i in range(length):
        child_time_list[i] += (length-i)
    time_list[index] = max(child_time_list)
    return time_list[index]

call_time(0)
print(time_list[0])
