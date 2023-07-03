# https://www.acmicpc.net/problem/2805

import sys

n, m = list(map(int, sys.stdin.readline().split()))
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)
highest = 0

while True:
    if start > end:
        break

    mid = (start + end) // 2

    # 현재 설정한 높이로 가져갈 수 있는 나무의 총량 계산
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid

    # 가져가야 할 높이보다 총량이 작은 경우, 절단기를 더 낮게 설정
    if total < m:
        end = mid - 1

    # 가져가야 할 높이보다 총량이 큰 경우, 절단기를 더 높이 설정
    # 해당하는 답을 찾았더라도 최적값(절단기 최대 높이)을 찾기 위해 계속 탐색
    elif total >= m:
        highest = mid
        start = mid + 1

print(highest)