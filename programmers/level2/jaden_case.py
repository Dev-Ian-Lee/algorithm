# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    
    size = len(s)
    for i in range(size):
        if i == 0:
            # 맨 처음 문자가 소문자인 경우, 대문자로 변환해 추가
            if ord('a') <= ord(s[i]) <= ord('z'):
                answer += s[i].upper()
                
            # 맨 처음 문자가 이미 대문자이거나 숫자인 경우, 그대로 추가
            else:
                answer += s[i]
        
        if i != 0:
            # 각 단어의 첫 문자가 소문자일 경우, 대문자로 변환해 추가
            if s[i - 1] == ' ' and ord('a') <= ord(s[i]) <= ord('z'):
                answer += s[i].upper()
                
            # 단어의 중간 문자가 대문자인 경우, 소문자로 변환해 추가
            elif s[i - 1] != ' ' and ord('A') <= ord(s[i]) <= ord('Z'):
                answer += s[i].lower()
                
            # 단어의 중간 문자가 소문자인 경우, 단어의 첫 문자가 숫자인 경우, 단어가 공백인 경우 그대로 추가
            else:
                answer += s[i]
    
    return answer