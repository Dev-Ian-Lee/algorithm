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
    for city in cities:
        if city < mid:
            total += city

        else:
            total += mid

    if total <= m:
        highest = mid
        start = mid + 1

    elif total > m:
        end = mid - 1

print(highest)