import sys

num_list = list()
for i in range(9):
    num_list.append(int(sys.stdin.readline()))
maximum = max(num_list)
print(maximum)
print(num_list.index(maximum)+1)
