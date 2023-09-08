# https://www.acmicpc.net/problem/11403

import copy

N = int(input())
nodes = [i for i in range(N)]

adj = []
for _ in range(N):
    adj.append(list(map(int, input().split())))
    
# 간선이 직접적으로 연결되어있는 경우(adj[i][j] == 1)는 1로 설정
visited = copy.deepcopy(adj)

# 각 노드 별로 dfs 
def dfs(start, adj):
    stack = []
    stack.append(start)
    
    while stack:
        popped = stack.pop()
        
        # 탐색을 시작한 노드와 직접적으로 연결된 노드 스택에 삽입
        if start == popped:
            for i in range(N):
                if adj[start][i] == 1:
                    stack.append(i)
        
        else:
            # 탐색을 시작한 노드로 돌아가는 경로가 있는 경우
            if adj[popped][start] == 1:
                visited[start][start] = 1
            
            # 탐색을 시작한 노드에서 다른 노드를 거쳐가는 경로가 있는 경우
            for i in range(N):
                if (visited[start][popped] == 1 and adj[popped][i] == 1) and visited[start][i] == 0:
                    visited[start][i] = 1
                    stack.append(i)

for node in nodes:
    dfs(node, adj)
    
for row in visited:
    for ele in row:
        print(ele, end = " ")
        
    print()