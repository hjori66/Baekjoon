import sys

A, B, C = map(int, sys.stdin.readline().split())
print(((C-A-1) // (A-B)) + 2)
