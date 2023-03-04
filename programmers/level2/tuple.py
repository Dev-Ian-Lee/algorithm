# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    ls = conversion(s)
    
    answer = []
    
    for ele in ls:
        for e in ele:
            if e not in answer:
                answer.append(e)
    
    return answer

def conversion(s):
    s = s.replace("{{", "")
    s = s.replace("}}", "")
    splitted = s.split("},{")
    
    converted = []
    
    for ele in splitted:
        tmp = ele.split(",")
        
        converted.append(list(map(int, tmp)))
        
    converted.sort(key = lambda x : len(x))
    return converted