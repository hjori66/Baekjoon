import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if N > 0 and M > 0:
    print(1)
elif N < 0 and M > 0:
    print(2)
elif N < 0 and M < 0:
    print(3)
else:
    print(4)
