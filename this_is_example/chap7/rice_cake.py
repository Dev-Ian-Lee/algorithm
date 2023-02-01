# <이것이 취업을 위한 코딩 테스트다> 실전 문제 7-5

# 초기 코드 : 적어도 M만큼의 떡을 얻는 것이 문제의 조건이므로 sum == M 이 아니라
# sum > M인 경우일 때도 종료되는 경우가 있을 수 있는데 이를 고려하지 못해서 틀림
# N, M = map(int, input().split())
# cakes = list(map(int, input().split()))
# cakes.sort()

# def binary_search(cakes, start, end):
#     if start > end:
#         return None
    
#     mid = (start + end) // 2

#     sum = 0
#     for cake in cakes:
#         if cake > cakes[mid]:
#             sum += cake - cakes[mid]

#     if sum == M:
#         return cakes[mid]
    
#     elif sum > M:
#         return binary_search(cakes, mid + 1, end)

#     else:
#         return binary_search(cakes, start, mid - 1)
    
# print(binary_search(cakes, 0, len(cakes) - 1))

# 개선 코드
N, M = map(int, input().split())
cakes = list(map(int, input().split()))

# 떡의 최소 길이와 최대 길이 사이값으로 자르기
start = 0
end = max(cakes)

result = 0
while start <= end:
    sum = 0
    mid = (start + end) // 2

    for cake in cakes:
        if cake > mid:
            sum += cake - mid

    # 떡의 양이 부족한 경우 더 많이 자르기 위해 왼쪽 부분 탐색
    if sum < M:
        end = mid - 1

    # 떡의 양이 충분한 경우(같거나 큰 경우) 덜 자르기 위해 오른쪽 부분 탐색
    else:
        # 현재가 최댓값인지 한 번 더 반복했을 때가 최댓값인지 모르기 때문에 일단 result 변수에 저장
        result = mid
        start = mid + 1
        
print(result)