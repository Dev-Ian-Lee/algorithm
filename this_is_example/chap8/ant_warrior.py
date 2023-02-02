# <이것이 취업을 위한 코딩 테스트다> 실전 문제 8-3

N = int(input())
storage = list(map(int, input().split()))

dp = [0] * N
dp[0] = storage[0]
dp[1] = storage[1]

for i in range(2, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + storage[i])

print(dp[-1])