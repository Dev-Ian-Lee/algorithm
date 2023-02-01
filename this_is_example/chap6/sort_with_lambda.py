# <이것이 취업을 위한 코딩 테스트다> 예제 6-6

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

# 람다 함수 사용해 정렬 기준 설정
result = sorted(array, key = lambda x : x[1])
print(result)