# https://www.acmicpc.net/problem/17225

import sys
from collections import deque

a, b, n = list(map(int, sys.stdin.readline().split()))

# 선물 포장을 시작하는 시간 저장
sangmin_queue = deque()
jisoo_queue = deque()
for _ in range(n):
    t, c, m = list(sys.stdin.readline().split())

    # 이전 선물 포장이 끝나지 않았을 경우, (이전 선물 포장이 끝나는 시간 + 포장에 걸리는 시간)과 포장 시작 시간 중 더 큰 값을 저장
    if c == "B":
        for i in range(int(m)):
            if len(sangmin_queue) != 0 and (sangmin_queue[-1] + a > int(t) + (a * i)):
                sangmin_queue.append(sangmin_queue[-1] + a)

            else:
                sangmin_queue.append(int(t) + (a * i))

    else:
        for i in range(int(m)):
            if len(jisoo_queue) != 0 and (jisoo_queue[-1] + b > int(t) + (b * i)):
                jisoo_queue.append(jisoo_queue[-1] + b)

            else:
                jisoo_queue.append(int(t) + (b * i))

sangmin = []
jisoo = []
present_num = 1
while True:
    # 둘 중 한 명이 먼저 끝난 경우, 다른 사람의 queue에 남은 선물 모두 반영
    if len(sangmin_queue) == 0:
        for _ in range(len(jisoo_queue)):
            jisoo.append(present_num)
            present_num += 1
        
        break

    elif len(jisoo_queue) == 0:
        for _ in range(len(sangmin_queue)):
            sangmin.append(present_num)
            present_num += 1

        break

    # 두 사람의 queue의 첫 항목을 비교해 포장 시작 시간이 더 빠른 선물을 먼저 포장
    if sangmin_queue[0] <= jisoo_queue[0]:
        sangmin.append(present_num)
        sangmin_queue.popleft()

    else:
        jisoo.append(present_num)
        jisoo_queue.popleft()

    present_num += 1

print(len(sangmin))
for s in sangmin:
    print(s, end = " ")

print()

print(len(jisoo))
for j in jisoo:
    print(j, end = " ")

print()