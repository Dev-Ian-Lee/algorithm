# https://school.programmers.co.kr/learn/courses/30/lessons/87946#

# 재귀함수 사용 시 필요한 변수 global로 선언 고려
answer = 0
visited = []

def solution(k, dungeons):
    global visited
    visited = [0] * len(dungeons)
    dfs(k, dungeons, 0)

    return answer

def dfs(k, dungeons, cnt):
    global answer, visited
    
    # dfs를 사용해 모든 경우의 수를 고려했을 때 가장 높은 cnt값 반환
    if cnt > answer:
        answer = cnt
    
    for i in range(len(dungeons)):
        least = dungeons[i][0]
        consume = dungeons[i][1]
        
        if k >= least and visited[i] == 0:
            # 현재 던전 방문한 뒤 다음 던전 방문
            visited[i] = 1
            dfs(k - consume, dungeons, cnt + 1)

            # 방문하지 않는 경우도 고려
            visited[i] = 0