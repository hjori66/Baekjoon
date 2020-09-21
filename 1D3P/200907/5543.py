import sys

num_list = list()
for i in range(5):
    num_list.append(int(sys.stdin.readline()))
print(min(num_list[0:3]) + min(num_list[3:5]) - 50)
