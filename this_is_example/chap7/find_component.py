# <이것이 취업을 위한 코딩 테스트다> 실전 문제 7-4

# 초기 코드
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    else:
         return binary_search(array, target, mid + 1, end)

N = int(input())
components = list(map(int, input().split()))
components.sort()

M = int(input())
orders = list(map(int, input().split()))

for order in orders:
    if binary_search(components, order, 0, len(components) - 1) != None:
        print('yes', end = ' ')

    else:
        print('no', end = ' ')

print()

# 계수 정렬을 이용한 방법
# N = int(input())
# count = [0] * 1000001

# for i in input().split():
#     count[int(i)] += 1

# M = int(input())
# orders = list(map(int, input().split()))

# for order in orders:
#     if count[order] == 1:
#          print('yes', end = ' ')

#     else:
#         print('no', end = ' ')

# print()

# 집합을 이용하는 방법
# N = int(input())
# components = set(map(int, input().split()))

# M = int(input())
# orders = list(map(int, input().split()))

# for order in orders:
#     if order in components:
#          print('yes', end = ' ')

#     else:
#         print('no', end = ' ')

# print()