# https://www.acmicpc.net/problem/2170

# 걸린 시간: 30min
# 시간복잡도: O(N)
# x, y 좌표가 -1억 ~ 1억이기 때문에 좌표를 배열 형태로 구현해 for문으로 검사 시 시간 초과날 것 같았음
# 현재 선의 시작점이 이전 선의 끝점보다 작은 경우, 두 선을 연결하는 방식으로 접근
# 이를 위해 선을 오름차순으로 정렬
# 현재 선의 시작점이 이전 선의 끝점보다 큰 경우는 새로운 선으로 취급

import sys

N = int(sys.stdin.readline())

lines = []
for _ in range(N):
    lines.append(list(map(int, sys.stdin.readline().split())))

def solution(N, lines):
    if N == 1:
        return lines[0][1] - lines[0][0]

    # 선 오름차순 정렬 후, 가장 왼쪽 선부터 시작
    lines.sort()
    start, end = lines[0][0], lines[0][1]

    compressed = []
    for line in lines[1:]:
        fr, to = line[0], line[1]
        
        # 현재 선의 시작점이 이전 선의 끝점보다 작은 경우, 두 선을 연결
        if fr <= end:
            if to > end:
                end = to
            
        # 현재 선의 시작점이 이전 선의 끝점보다 큰 경우, 새로운 선 시작
        else:
            compressed.append([start, end])
            start, end = fr, to

    # 모든 선이 하나로 연결된 경우 고려
    if len(compressed) == 0:
        compressed.append([start, end])

    # 마지막 선 고려
    if start != compressed[-1][0] or end != compressed[-1][1]:
        compressed.append([start, end])

    total = 0
    for line in compressed:
        total += line[1] - line[0]

    return total

print(solution(N, lines))