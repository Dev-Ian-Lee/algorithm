# <이것이 취업을 위한 코딩 테스트다> 실전 문제 5-8

from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

    return graph[N - 1][M - 1]

print(bfs(0, 0))