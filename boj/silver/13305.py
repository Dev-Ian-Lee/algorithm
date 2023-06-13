# https://www.acmicpc.net/problem/13305

n = int(input())
roads = list(map(int, input().split()))
stations = list(map(int, input().split()))

answer = 0
cheapest = int(1e9)

# 더 싼 주유소가 나오기 전까지 현재 주유소에서 주유
for i in range(len(roads)):
    if stations[i] < cheapest:
        cheapest = stations[i]
    
    answer += cheapest * roads[i]

print(answer)