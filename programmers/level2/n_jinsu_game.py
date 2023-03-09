# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    s = ""
    
    # 문자열 s에 0부터 100000까지의 n진수를 연결해 저장
    for i in range(0, 100000):
        s += convert(i, n)
    
    result = ""
    
    # 첫 번로 (순서 - 1)번째 수를 말하고, 그 다음부터는 참가자 수인 m번째 뒤를 말함
    for i in range(p - 1, len(s) - 1, m):
        result += s[i]
        
        # 말해야하는 숫자 개수를 다 채우면 종료
        if len(result) == t:
            break
            
    return result    
    
# num을 n진수로 변환해 반환
def convert(num, n):

    # 0은 모든 진수에서 "0"
    if num == 0:
        return "0"
    
    ls = []
    
    while True:
        if num < 1:
            break
            
        mod = num % n
        
        if mod >= 10 and mod <= 15:
            ls.append(chr(mod + 55))
            
        else:
            ls.append(str(mod))
            
        num = num // n
        
    s = ""
    for i in range(len(ls) - 1, -1, -1):
        s += ls[i]
        
    return s