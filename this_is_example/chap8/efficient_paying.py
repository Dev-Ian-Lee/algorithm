# <이것이 취업을 위한 코딩 테스트다> 실전 문제 8-5

N, M = map(int, input().split())
currencies = []

for _ in range(N):
    currencies.append(int(input()))

dp = [10001] * (M + 1)
dp[0] = 0

for currency in currencies:
    for i in range(currency, M + 1):
        if dp[i - currency] != 10001:
            dp[i] = min(dp[i], dp[i - currency] + 1)

if dp[M] != 10001:
    print(dp[M])

else:
    print(-1)