# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    dic = [chr(i + 65) for i in range(26)]
    idx_log = []
    
    idx = 0
    s = msg[0]
    size = len(msg)
    
    while True:
        if idx >= size:
            break
        
        # 현재 문자열이 사전에 있는 경우, 다음 문자도 더해서 고려
        if s in dic:
            idx += 1
            
            # 현재 문자열이 사전에 있기 때문에, 마지막 인덱스에 도달하면 현재 문자열의 인덱스 로그에 추가
            if idx == size:
                idx_log.append(dic.index(s) + 1)
                break
                
            s += msg[idx]

        # 현재 문자열이 사전에 없는 경우 사전에 더하고, 마지막 문자 더하기 전의 문자열의 인덱스 로그에 추가
        else:
            dic.append(s)
            idx_log.append(dic.index(s[:-1]) + 1)
            s = msg[idx]

    return idx_log