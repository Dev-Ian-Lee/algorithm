# https://www.acmicpc.net/problem/11053

# 걸린 시간: -
# 시간복잡도: O(N^2)

# dp 문제라는 건 알았는데 이중 for문으로 이전 항까지를 검사하는 방법을 생각 못해서 검색

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    
print(max(dp))