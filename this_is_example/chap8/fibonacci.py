# <이것이 취업을 위한 코딩 테스트다> 실전 문제 8-1

# 일반적 재귀
# def fibonacci(x):
#     if x == 1 or x == 2:
#         return 1
    
#     return fibonacci(x - 1) + fibonacci(x - 2)

# 메모이제이션 활용한 재귀
memo = [0] * 100

def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    
    # 이미 계산되어 메모에 저장된 값은 다시 계산하지 않고 메모를 불러옴
    if memo[x] != 0:
        return memo[x]
    
    # 저장되지 않은 값은 재귀적으로 계산한 뒤 메모에 저장
    memo[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return memo[x]

print(fibonacci(99))