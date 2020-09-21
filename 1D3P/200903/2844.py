import sys

N, M = map(int, sys.stdin.readline().split())

if M >= 45:
    print(N, M-45)
else:
    print((N-1)%24, M+15)
