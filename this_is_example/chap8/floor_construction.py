# <이것이 취업을 위한 코딩 테스트다> 실전 문제 8-4

N = int(input())

dp = [0] * N
dp[0] = 1
dp[1] = 3

for i in range(2, N):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[-1] % 796796)