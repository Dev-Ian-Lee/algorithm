# <이것이 취업을 위한 코딩 테스트다> 예제 6-2

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        
        # 더 작은 원소를 만나면 그 위치에서 멈춤
        else:
            break

print(array)