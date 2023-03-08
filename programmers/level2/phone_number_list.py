# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    dic = {}
    
    # 리스트를 딕셔너리로 변환
    for num in phone_book:
        dic[num] = 1
        
    for key in dic:
        tmp = ""
        
        # 딕셔너리의 각 키를 앞에서부터 잘라서 만든 문자열과 같은 문자열이 있으면 False 반환
        for c in key:
            tmp += c
            
            if (tmp in dic) and (tmp != key):
                return False
        
    return True