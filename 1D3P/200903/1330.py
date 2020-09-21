import sys

N, C = map(int, sys.stdin.readline().split())

if N > C:
    print(">")
if N < C:
    print("<")
if N == C:
    print("==")
