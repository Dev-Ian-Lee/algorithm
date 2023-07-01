# https://www.acmicpc.net/problem/2606

import sys
from collections import deque

n = int(sys.stdin.readline())
e = int(sys.stdin.readline())

edges = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b = list(map(int, sys.stdin.readline().split()))
    edges[a].append(b)
    edges[b].append(a)

start = 1
visited = [False] * (n + 1)

def bfs(start):
    queue = deque([start])
    
    while queue:
        popped = queue.popleft()
        
        for adjacent in edges[popped]:
            if visited[adjacent] == False:
                queue.append(adjacent)
                visited[adjacent] = True

    # 1번 컴퓨터는 제외하고 감염된 컴퓨터 수 계산
    visited[start] = False

    infested = 0
    for node in visited:
        if node == True:
            infested += 1

    return infested

print(bfs(start))