# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

n, m, start = list(map(int, sys.stdin.readline().split()))

edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    edges[a].append(b)
    edges[b].append(a)

def dfs(edges):
    stack = [start]
    visited = []

    while stack:
        popped = stack.pop()

        if popped not in visited:
            visited.append(popped)

            # 작은 번호 먼저 방문하기 위해 역순으로 정렬
            edges[popped].sort(reverse = True)
            for adjacent in edges[popped]:
                stack.append(adjacent)

    for node in visited:
        print(node, end = " ")

    print()
    
def bfs(edges):
    queue = deque([start])
    visited = [start]

    while queue:
        popped = queue.popleft()

        # 작은 번호 먼저 방문하기 위해 정렬
        edges[popped].sort()
        for adjacent in edges[popped]:
            if adjacent not in visited:
                queue.append(adjacent)
                visited.append(adjacent)

    for node in visited:
        print(node, end = " ")

    print()

dfs(edges)
bfs(edges)