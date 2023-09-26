# https://school.programmers.co.kr/learn/courses/30/lessons/17683

# 걸린 시간: -
# 시간복잡도: O(N * M)

# A#을 a로 변환해서 풀기(replace 사용)
# 문제 조건 잘 읽기

def solution(m, musicinfos):
    answer = []
    num = 1
    
    # "#" 포함하는 음은 소문자로 대체
    if "#" in m:
        m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    for info in musicinfos:
        start, end, title, notes = info.split(",")
        runtime = 0
        total = ""
        
        if "#" in notes:
            notes = notes.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        
        # 재생시간 계산
        start_time = int(start[:2]) * 60 + int(start[3:])
        end_time = int(end[:2]) * 60 + int(end[3:])
        runtime = end_time - start_time
            
        # 재생시간이 음악 길이보다 긴 경우, 반복 재생
        if runtime > len(notes):
            div, mod = divmod(runtime, len(notes))
            total = (notes * div) + notes[:mod]
            
        # 재생시간이 음악 길이보다 작은 경우, 일부만 재생
        elif runtime < len(notes):
            total = notes[:runtime]    
        
        else:
            total = notes[:]
        
        if m in total:
            answer.append([runtime, num, title])
            num += 1
    
    if len(answer) == 0:
        return "(None)"
    
    elif len(answer) == 1:
        return answer[0][2]
    
    # 조건이 일치하는 음악이 여러 개일 경우, 재생 시간이 긴 순서대로, 먼저 입력된 순서대로 정렬
    else:
        answer.sort(key = lambda x : (-x[0], x[1]))
        return answer[0][2]

# 반례
# print(solution("A#", ["12:00,12:01,HELLO,A#"]))
# print(solution("CC#BCC#BCC#", ["03:00,03:08,FOO,CC#B"]))
