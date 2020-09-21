import sys

num_list = list()
for i in range(10):
    num_list.append(int(sys.stdin.readline()) % 42)
num_list = list(set(num_list))
print(len(num_list))
