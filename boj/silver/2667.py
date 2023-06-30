# https://www.acmicpc.net/problem/2667

import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

def bfs(start):
    queue = deque([[start[0], start[1]]])
    graph[start[0]][start[1]] = 0
    house_count = 1
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # queue에 넣을 때 방문 처리해야 메모리 초과가 발생하지 않음
            if (nx >= 0 and nx < n) and (ny >= 0 and ny < n):
                if graph[nx][ny] == 1:
                    queue.append([nx, ny])
                    graph[nx][ny] = 0
                    house_count += 1

    return house_count

# 단지의 수는 bfs를 시행한 횟수
block_count = 0
house_counts = []
while True:
    start = [-1, -1]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                start = [i, j]
                break

        if start != [-1, -1]:
            break

    if start == [-1, -1]:
        break

    house_counts.append(bfs(start))
    block_count += 1

house_counts.sort()

print(block_count)
for ele in house_counts:
    print(ele)