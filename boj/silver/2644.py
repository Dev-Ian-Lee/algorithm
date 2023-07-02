# https://www.acmicpc.net/problem/2644

import sys
from collections import deque

n = int(sys.stdin.readline())
start, end = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

relationship = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    relationship[a].append(b)
    relationship[b].append(a)

visited = [0 for _ in range(n + 1)]

def bfs(start):
    queue = deque([start])

    while queue:
        popped = queue.popleft()

        for adjacent in relationship[popped]:

            # 부모 혹은 자식은 1촌 추가
            if visited[adjacent] == 0:
                visited[adjacent] = visited[popped] + 1
                queue.append(adjacent)

            if adjacent == end:
                return visited[adjacent]
    
    # 촌수 계산 불가능한 경우
    return -1

print(bfs(start))