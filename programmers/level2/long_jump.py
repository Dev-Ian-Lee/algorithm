# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    if n == 1:
        return 1
    
    dp = [0 for _ in range(n + 1)]
    dp[1], dp[2] = 1, 2
    
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
        
    return dp[-1]