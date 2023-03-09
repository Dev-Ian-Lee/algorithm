# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    dic = []
    idx = 27
    idx_log = []
    
    for i in range(1, idx):
        dic.append(chr(64 + i))
    
    size = len(msg)
    
    i = 0
    s = msg[0]
    
    while True:
        if i >= size:
            break
        
        # 현재 문자열이 사전에 있는 경우, 다음 문자도 더해서 고려
        if s in dic:
            i += 1
            
            # 마지막 한 문자는 알파벳 대문자 중 하나이기 때문에 사전에 반드시 존재
            if i == size:
                idx_log.append(dic.index(s) + 1)
                break
                
            s += msg[i]

        # 현재 문자열이 사전에 없는 경우 사전에 더하고, 마지막 문자 더하기 전의 문자열의 인덱스 로그에 추가
        else:
            dic.append(s)
            idx_log.append(dic.index(s[:-1]) + 1)
            s = msg[i]

    return idx_log