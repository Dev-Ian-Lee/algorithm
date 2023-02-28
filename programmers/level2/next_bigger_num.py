# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    num_of_one = bin(n).count("1")
    
    for i in range(n + 1, 1000001):
        if bin(i).count("1") == num_of_one:
            return i