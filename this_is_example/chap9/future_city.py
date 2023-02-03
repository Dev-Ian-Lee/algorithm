# <이것이 취업을 위한 코딩 테스트다> 실전 문제 9-4

INF = int(1e9)

N, M = map(int, input().split())

graph = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

X, K = map(int, input().split())

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if graph[1][K] != INF and graph[K][X] != INF:
    print(graph[1][K] + graph[K][X])

else:
    print(-1)