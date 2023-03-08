# https://school.programmers.co.kr/learn/courses/30/lessons/92335

import math

def solution(n, k):
    converted = convert(n, k)
    splitted = converted.split("0")
    ls = []
    
    for ele in splitted:
        if len(ele) != 0:
            if is_prime(int(ele)):
                ls.append(ele)
    
    return len(ls)

# n을 k진수로 변환
def convert(n, k):

    # 10진수면 문자열로 변환해서 그대로 반환
    if k == 10:
        return str(n)
    
    ls = []
    
    while True:
        if n <= 0:
            break
            
        ls.append(n % k)
        n = n // k
        
    s = ""
    
    for i in range(len(ls) - 1, -1, -1):
        s += str(ls[i])
        
    return s

def is_prime(num):
    if num == 1:
        return False
    
    # num - 1 까지 다 할 필요 없이, num의 제곱근까지만 고려하면 소수 판별 가능
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True