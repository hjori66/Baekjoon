import sys

while True:
    line = sys.stdin.readline()
    if line[0] == '0':
        break
    N, Q = map(int, line.split())
    if N == 1:
        num_list = [int(sys.stdin.readline())]
    else:
        num_list = list(map(int, sys.stdin.readline().split()))

    temp = 0
    start_list = list()
    occurency_list = list()
    for i, num in enumerate(num_list):
        if i == 0:
            start_list.append(i)
        elif num_list[i-1] != num:
            occurency_list.append(i - temp)
            start_list.append(i)
            temp = i
    occurency_list.append(len(num_list) - temp)

    for _ in range(Q):
        left, right = map(int, sys.stdin.readline().split())
        left -= 1
        right -= 1

        left_index = 0
        right_index = len(start_list) - 1
        for i, start in enumerate(start_list):
            if start <= left:
                left_index = i
            if start <= right:
                right_index = i
        occurency = 0
        if right_index == left_index:
            occurency = right - left + 1
        else:
            if right_index - left_index > 1:
                occurency = max(occurency_list[left_index+1:right_index])
            left_occurency = start_list[left_index+1]-left
            right_occurency = right-start_list[right_index]+1
            occurency = max(occurency, left_occurency, right_occurency)
        print(occurency)
