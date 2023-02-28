# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    size = len(words)
    mem = set()
    pre = ""
    
    for i in range(size):
        curr = words[i]
        
        if i == 0:
            mem.add(curr)
            pre = curr
            continue
        
        # 현재 단어가 이미 나왔을 경우 탈락자 발생
        if curr in mem:
            return finish_game(i, n)
            
        else:
            if pre[-1] == curr[0]:
                mem.add(curr)
                pre = curr
                
            # 이전 단어의 마지막 글자와 현재 단어의 첫 글자가 다를 경우 탈락자 발생
            else:
                return finish_game(i, n)

    return [0, 0]

# 탈락한 사람의 번호와 차례 계산
def finish_game(i, n):
    player = (i + 1) % n

    if player == 0:
        player = n

    turns = 0
    if (i + 1) % n == 0:
        turns = (i + 1) // n

    else:
        turns = ((i + 1) // n) + 1

    return [player, turns]