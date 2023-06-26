# https://www.acmicpc.net/problem/14719

import sys

h, w = list(map(int, sys.stdin.readline().split()))
ls = list(map(int, sys.stdin.readline().split()))

acc = 0
for i in range(1, w - 1):
    # 현재 블록 기준 왼쪽에서 가장 높은 블록
    left = max(ls[:i])

    # 현재 블록 기준 오른쪽에서 가장 높은 블록
    right = max(ls[i + 1:])

    # 둘 중 더 낮은 블록이 기준
    base = min(left, right)

    # 기준 블록보다 낮은 칸에 물이 고임
    if ls[i] < base:
        acc += base - ls[i]

print(acc)