import sys

a = sys.stdin.readline
n = int(a())
b = [0] * 10000
for _ in range(n):
    b[_] = int(a())

dp = [0] * 10000
dp[0] = b[0]
dp[1] = b[0] + b[1]
dp[2] = max(dp[1], b[1]+b[2], b[0]+b[2])
for i in range(3,n):
    dp[i] = max(dp[i-3] + b[i] + b[i-1], dp[i-2] + b[i], dp[i-1])

print(dp[n])