import sys

num_list = list()
for _ in range(7):
    num = int(sys.stdin.readline())
    if num % 2 == 1:
        num_list.append(num)

if not num_list:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))
