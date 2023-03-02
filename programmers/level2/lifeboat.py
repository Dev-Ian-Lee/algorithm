# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    cnt = 0
    people.sort(reverse = True)
    people = deque(people)
    
    while True:
        if len(people) == 0:
            break
        
        # 가장 무거운 사람과 가장 가벼운 사람이 함께 탑승
        if people[0] + people[-1] <= limit and len(people) >= 2:
            people.popleft()
            people.pop()
            
        # 가장 무거운 사람 혼자 탐승
        else:
            people.popleft()
            
        cnt += 1
    
    return cnt