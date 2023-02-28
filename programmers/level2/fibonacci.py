# https://school.programmers.co.kr/learn/courses/30/lessons/12945

# 파이썬은 다른 언어보다 최대 재귀 깊이가 낮기 때문에 아래와 같이 최대 재귀 깊이를 늘려주면 런타임 에러 해결 가능
import sys
sys.setrecursionlimit(10 ** 6)

dp = [0] * 100001

def solution(n):
    if n == 0 or n == 1:
        dp[n] = n
        return dp[n]
    
    if dp[n] != 0:
        return dp[n]
    
    else:
        dp[n] = (solution(n - 2) + solution(n - 1)) % 1234567
    
    return dp[n]