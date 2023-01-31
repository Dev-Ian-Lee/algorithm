# <이것이 취업을 위한 코딩 테스트다> 예제 6-3

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 리스트의 원소가 1개인 경우 종료
    if start >= end:
        return 

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 왼쪽에서 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 오른쪽에서 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
        else:
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 리스트와 오른쪽 리스트로 정렬
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)