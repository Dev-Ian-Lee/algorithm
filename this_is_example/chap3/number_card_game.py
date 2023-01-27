# <이것이 취업을 위한 코딩 테스트다> 실전 문제 3-3

N, M = map(int, input().split())
min_of_rows = []

for _ in range(N):
    row = list(map(int, input().split()))
    min_of_rows.append(min(row))

print(max(min_of_rows))