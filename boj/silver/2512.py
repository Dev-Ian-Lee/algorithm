# https://www.acmicpc.net/problem/2512

import sys

n = int(sys.stdin.readline())
cities = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 1
end = max(cities)
highest = 0
while True:
    if start > end:
        break

    mid = (start + end) // 2

    total = 0

    # 요청된 예산이 mid보다 작을 경우에는 요청된 예산을, 더 클 경우 mid를 total에 누적
    for city in cities:
        if city < mid:
            total += city

        else:
            total += mid

    # total이 예산총액을 넘지 않았을 경우 더 큰 범위를 탐색
    # 최적값이 나올 때까지 수행
    if total <= m:
        highest = mid
        start = mid + 1

    # 넘었을 경우 더 작은 범위를 탐색
    elif total > m:
        end = mid - 1

print(highest)