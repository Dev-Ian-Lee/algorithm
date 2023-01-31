# <이것이 취업을 위한 코딩 테스트다> 예제 6-1

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 가장 작은 원소의 인덱스
    min_index = i

    for j in range(i + 1, len(array)):
        # i번째 원소보다 작은 j번째 원소를 찾을 때마다 바꾸지 않고, 각 반복에서 가장 작은 원소의 인덱스를 구하고 원소를 한 번만 바꿈
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print(array)