# https://www.acmicpc.net/problem/10815

import sys

n = int(sys.stdin.readline())
owned = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

owned.sort()
ls = []
check_idx = 0

while True:
    # 모든 숫자를 확인했을 경우 종료
    if len(ls) == m:
        break

    start = 0
    end = len(owned) - 1

    while True:
        # check의 숫자가 owned에 없을 경우
        if start > end:
            ls.append(0)
            check_idx += 1
            break

        mid = (start + end) // 2

        # 현재 숫자가 owned의 중앙에 있는 경우
        if check[check_idx] == owned[mid]:
            ls.append(1)
            check_idx += 1
            break

        # 현재 숫자가 더 큰 경우, 오른쪽 탐색
        elif check[check_idx] > owned[mid]:
            start = mid + 1

        # 현재 숫자가 더 작은 경우, 왼쪽 탐색
        elif check[check_idx] < owned[mid]:
            end = mid - 1

for ele in ls:
    print(ele, end = " ")

print()