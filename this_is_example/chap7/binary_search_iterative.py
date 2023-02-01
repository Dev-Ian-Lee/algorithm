# <이것이 취업을 위한 코딩 테스트다> 예제 7-3

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None

N, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, N - 1)

if result == None:
    print('원소가 존재하지 않습니다.')

else:
    print(result + 1)