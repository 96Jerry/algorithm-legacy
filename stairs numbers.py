# 쉬운 계단수
# 2차원 배열을 활용한 동적프로그래밍
# 간단한 수식 만드는 것 습관화 ex) 7번 째 줄에 dp = [[0]*10 for _ in range(n+1)] 

n = int(input())

dp = [[0]*10 for _ in range(n+1)]

dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2,n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

answer = sum(dp[n])

print(answer)

