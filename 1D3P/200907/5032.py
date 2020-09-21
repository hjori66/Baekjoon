import sys

A, B, C = map(int, sys.stdin.readline().split())
print(max(0, (A+B-1) // (C-1)))
