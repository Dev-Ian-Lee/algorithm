# https://school.programmers.co.kr/learn/courses/30/lessons/12899

# 걸린 시간: 40min
# 시간복잡도: O(log N)
# 1, 2, 4가 반복되기 때문에 3으로 나눈 몫과 나머지 활용
# 이전 값이 이후 값에 영향 -> DP 사용해 n까지의 모든 값에 대해 반복(bottom-up) -> 시간 초과 발생
# n <= 50,000,000이므로 O(N)이어도 시간 초과

# 어차피 n에 대한 값만 알고 싶은 것이기 때문에 재귀적으로 필요한 값만 계산해 해결(top-down)

import sys
sys.setrecursionlimit(10**6)

def solution(n):
    return str(recursion(n))

def recursion(n):
    # 종료 조건(재귀 과정에서 n이 0이 되는 경우가 있어서 0도 고려해야 함)
    if n in [0, 1, 2]:
        return n
    
    if n % 3 == 0:
        return 10 * recursion(n // 3 - 1) + 4
            
    else:
        return 10 * recursion(n // 3) + (n % 3)
    
# 이전 코드(시간 초과)
# def solution(n):
#     dp = [0 for _ in range(n + 1)]
    
#     for i in range(1, len(dp)):
#         if i % 3 == 0:
#             dp[i] = 10 * dp[i // 3 - 1] + 4
            
#         else:
#             dp[i] = 10 * dp[i // 3] + (i % 3)
    
#     return str(dp[-1])