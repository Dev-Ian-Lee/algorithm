# https://www.acmicpc.net/problem/1080

# 걸린 시간: 70min
# 시간복잡도: O(N * M)

# 문제 유형이 그리디라는 걸 몰랐으면 해결 어려웠을 것 같음

import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())

    A = []
    for _ in range(N):
        A.append(list(map(int, list(sys.stdin.readline().rstrip()))))

    B = []
    for _ in range(N):
        B.append(list(map(int, list(sys.stdin.readline().rstrip()))))

    if A == B:
        return 0

    # 행렬의 크기가 3*3보다 작을 경우, 행렬 A를 B로 만들 수 없음 
    if (N < 3 or M < 3) and A != B:
        return -1

    operation_cnt = 0
    for i in range(N):
        for j in range(M):
            # 행렬 A를 앞에서부터 탐색해 현재 값이 행렬 B의 값과 다르면, 그리디하게 해당 위치에서 시작하는 3*3 크기의 부분 행렬 변환 
            if A[i][j] != B[i][j] and (i + 2 < N and j + 2 < M):
                for k in range(3):
                    for l in range(3):
                        if A[i + k][j + l] == 0:
                            A[i + k][j + l] = 1

                        else:
                            A[i + k][j + l] = 0

                operation_cnt += 1
                
            if A == B:
                return operation_cnt

    if A != B:
        return -1

print(solution())
