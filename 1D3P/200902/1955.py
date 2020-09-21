import sys, math

N = int(sys.stdin.readline())

dp = [0] * (N+1)
factorial = [1, 1, 2, 6, 24, 120, 720, 5040]

for i in range(1, N+1):
    dp[i] = i
    for j in range(1, i):
        dp[i] = min(dp[i], dp[j] + dp[i-j])
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            dp[i] = min(dp[i], dp[j] + dp[i//j])
    for j in range(2, 8):
        if i == factorial[j]:
            dp[i] = min(dp[i], dp[j])
print(dp[N])
