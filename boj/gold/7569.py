# https://www.acmicpc.net/problem/7569

# 걸린 시간: 70min
# 시간복잡도: O(H * N * M)

# BFS를 사용해 해결했기 때문에, 매 반복마다 종료 검사를 할 필요 없이 큐(덱)이 빈 경우에만 종료하면 됨
# while문 종료 후에만 삼중for문으로 box에 0(익지 않은 토마토)이 남아있는지 검사해 -1 반환
# [[[-1, 1], [1, -1]], [[-1, 1], [0, -1]]] 처럼 1(익은 토마토)이 고립된 경우가 있기 때문에, 처음 삼중for문에서 start만 찾는 것이 아닌, 1인 값을 모두 찾아서 큐에 추가

from collections import deque
import sys

def solution():
    M, N, H = map(int, sys.stdin.readline().split())
    
    # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]
    dz = [0, 0, -1, 1, 0, 0]

    # 토마토 상자, visited 입력
    box = []
    visited = []
    for _ in range(H):
        box_tmp = []
        visited_tmp = []
        for _ in range(N):
            box_tmp.append(list(map(int, sys.stdin.readline().split())))
            visited_tmp.append([0 for _ in range(M)])
            
        box.append(box_tmp)
        visited.append(visited_tmp)

    # 큐(덱)에 익은 토마토 좌표 모두 추가
    dq = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    dq.append((i, j, k))
            
    # BFS
    highest = 0
    while True:
        if len(dq) == 0:
            break
        
        x, y, z = dq.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            # nx, ny, nz가 상자 범위 내에 있고 해당 칸에 익지 않은 토마토가 있는 경우
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if box[nx][ny][nz] == 0:
                    box[nx][ny][nz] = 1
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    highest = visited[nx][ny][nz]
                    dq.append((nx, ny, nz))
                    
    # 익지 않은 토마토가 남은 경우 -1 반환
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    return -1
                    
    # visited에서 가장 큰 값(걸리는 일 수) 반환
    return highest
        
print(solution())