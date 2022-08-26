import sys

n = int(input())

a = []
dp = []

for i in range(n):
    a.append(int(sys.stdin.readline()))

if n == 1:
    print(a[0])
if n == 2:
    print(a[0]+a[1])
if n >= 3:
    dp.append(a[0])
    dp.append(a[0]+a[1])
    dp.append(max(a[0]+a[2],a[1]+a[2]))

    for i in range(3, n):
        dp.append(max(dp[i-2]+a[i],dp[i-3]+a[i]+a[i-1]))

    print(dp[-1])