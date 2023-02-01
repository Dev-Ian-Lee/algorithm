# <이것이 취업을 위한 코딩 테스트다> 예제 6-5

# 모든 원소의 값이 0이상이라고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언
count = [0] * (max(array) + 1)

for ele in array:
    count[ele] += 1

# 카운트된 횟수만큼 각 원소 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')

print()