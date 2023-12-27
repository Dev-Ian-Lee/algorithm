# https://www.acmicpc.net/problem/11660

# 걸린 시간: -
# 시간복잡도: O(N^2)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for i in range(N):
    ls = list(map(int, input().split()))
    arr.append(ls)
    
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + arr[i - 1][j - 1]
        
for k in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])