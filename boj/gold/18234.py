# https://www.acmicpc.net/problem/18234

import sys

n, t = list(map(int, sys.stdin.readline().split()))

# 모든 당근의 초기 맛의 총합
# t >= n이므로 반드시 모든 당근을 먹음
initial = 0

# 각 당근의 영양제
nutrition = []

for _ in range(n):
    carrots = list(map(int, sys.stdin.readline().split()))
    initial += carrots[0]
    nutrition.append(carrots[1])

increment = 0

# 건너뛸 날짜
# 맛의 총합이 가장 크게 먹기 위해서는 최대한 늦게 먹어야 함
# 예로, t = 10, n = 6이라면 처음 4일은 건너뛰고 마지막 6일동안 먹는 것이 최대
diff = t - n

# 영양제의 값이 작을수록 먼저 먹음
nutrition.sort()

for i in range(diff, t):
    increment += nutrition[i - diff] * i

# 초기 맛의 총합 + 증가한 맛의 총합
print(initial + increment)