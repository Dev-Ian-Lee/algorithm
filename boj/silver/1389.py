# https://www.acmicpc.net/problem/1389

# 걸린 시간: 35min
# 시간복잡도: O(N^3)

# 플로이드 워셜은 삼중 for문 i > j > k 순이 아닌, k > i > j 순으로 반복해야 함
# i > j > k 순으로 할 경우, 이후에 수정되는 다른 값을 사용할 수 없기 때문

import sys

N, M = map(int, sys.stdin.readline().split())

# 친구 관계 연결
adjacent = [[int(1e9) for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())

    adjacent[A][B] = 1
    adjacent[B][A] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # k(중간 단계)가 i나 j와 같을 경우 pass
            if i == k or j == k:
                continue

            # i와 j가 같은 사람이거나, 둘이 이미 친구일 경우 pass
            if i == j or adjacent[i][j] == 1:
                continue

            # 현재 값과 중간 단계를 거친 값 중 작은 값으로 갱신
            if adjacent[i][k] != int(1e9) and adjacent[k][j] != int(1e9):
                adjacent[i][j] = min(adjacent[i][j], adjacent[i][k] + adjacent[k][j])
                adjacent[j][i] = adjacent[i][j]

smallest = int(1e9)
ans = 0
for idx in range(1, N + 1):
    bacon = 0

    for ele in adjacent[idx]:
        if ele != int(1e9):
            bacon += ele

    if bacon < smallest:
        smallest = bacon
        ans = idx

print(ans)
