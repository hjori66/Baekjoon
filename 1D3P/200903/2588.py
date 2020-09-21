import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
print(N*(M%10))
print(N*((M//10)%10))
print(N*(M//100))
print(N*M)
