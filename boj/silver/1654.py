# https://www.acmicpc.net/problem/1654

import sys

k, n = list(map(int, sys.stdin.readline().split()))

lans = []
for _ in range(k):
    lans.append(int(sys.stdin.readline()))

start = 0
end = max(lans)
highest = 0
while True:
    if start > end:
        break

    mid = (start + end) // 2

    # start == 0, end == 1인 경우 mid가 1이 되고, 이 경우 모든 랜선을 길이 1로 잘라냄
    if mid == 0:
        mid = 1

    quantity = 0
    for lan in lans:
        quantity += lan // mid

    # 파라메트릭 서치
    # 잘라낸 개수가 n 이상일 경우 더 높은 mid값을 구하기 위해 start를 mid 이후로 옮김
    if quantity >= n:
        start = mid + 1
        highest = mid

    # n 미만일 경우 더 잘게 자르기 위해 end를 mid 이전으로 옮김
    else:
        end = mid - 1

print(highest)