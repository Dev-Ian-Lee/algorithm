# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    num_of_zero = 0
    cnt = 0
    
    while True:
        if s == "1":
            break
        
        cnt += 1
        num_of_zero += s.count("0")
        
        s = s.replace("0", "")
        size = len(s)
        s = bin(size)[2:]
        
    answer = [cnt, num_of_zero]
    return answer