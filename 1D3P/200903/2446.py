import sys

N = int(sys.stdin.readline())
for i in range(N):
    print(' ' * i + '*' * (2*N-2*i-1))
for i in range(N-1):
    print(' ' * (N-2-i) + '*' * (i*2+3))
