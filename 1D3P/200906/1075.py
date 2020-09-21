import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

start = (N//100)*100
if start % K == 0:
    print(str(start)[-2:])
else:
    print(str(start - (start % K) + K)[-2:])
