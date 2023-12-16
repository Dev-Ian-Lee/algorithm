# https://www.acmicpc.net/problem/1697

# 걸린 시간: 50min
# 시간복잡도: O(max(N, K))

# 플로이드 워셜 -> N, K 범위가 너무 커서 불가능
# DP -> 현재 값에서 -1, +1, *2 세 가지 경우를 고려해야하므로 인덱스 이동이 어려움
# 덱을 사용해서 BFS로 해결

from collections import deque

def solution():
    N, K = map(int, input().split())

    if N == K:
        return 0

    elif N > K:
        bigger = N
        
    else:
        bigger = K

    # 현재 값에 2를 곱한 값이 K를 넘더라도, 2를 곱한 뒤에 1을 반복해서 차감하는 것이 더 빠른 경우도 있음
    # 따라서, 배열의 크기를 N, K 중 더 큰 값의 2배로 설정
    adjacent = [int(1e9) for _ in range(bigger * 2 + 1)]
    adjacent[N] = 0
    
    last = len(adjacent) - 1

    dq = deque()
    dq.append(N)
    while True:
        if len(dq) == 0:
            break
        
        curr = dq.popleft()
        
        # 현재 값에서 -1, +1, *2 한 계산값의 범위가 유효하고, (현재 값 + 1)보다 큰 경우 값을 갱신
        # 다음 반복을 위해 덱에 계산값 삽입
        if 0 <= curr - 1 <= last:
            if adjacent[curr - 1] > adjacent[curr] + 1:
                adjacent[curr - 1] = adjacent[curr] + 1
                dq.append(curr - 1)
            
        if 0 <= curr + 1 <= last:
            if adjacent[curr + 1] > adjacent[curr] + 1:
                adjacent[curr + 1] = adjacent[curr] + 1
                dq.append(curr + 1)
            
        if 0 <= curr * 2 <= last:
            if adjacent[curr * 2] > adjacent[curr] + 1:
                adjacent[curr * 2] = adjacent[curr] + 1
                dq.append(curr * 2)
        
    return adjacent[K]
    
print(solution())