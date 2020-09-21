import sys

N = int(sys.stdin.readline())
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    ans = ((A%10)**(B%4+4))%10
    if ans == 0:
        print(10)
    else:
        print(ans)
