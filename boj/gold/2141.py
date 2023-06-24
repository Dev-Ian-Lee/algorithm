# https://www.acmicpc.net/problem/2141

import sys

n = int(sys.stdin.readline())

total_population = 0
villages = []
for _ in range(n):
    village_num, population = list(map(int, sys.stdin.readline().split()))
    total_population += population
    villages.append([village_num, population])

villages.sort()

# 총 인구의 과반이 넘는 마을에 우체국 건설
acc = 0
for v in villages:
    acc += v[1]

    if acc >= total_population / 2:
        print(v[0])
        break