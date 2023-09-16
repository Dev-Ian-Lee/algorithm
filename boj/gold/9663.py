# https://www.acmicpc.net/problem/9663

# 걸린 시간: -
# 시간복잡도: O(N!)

# Python3로 제출 시 시간 초과 발생, Pypy3로 제출 시 성공
# 이차원 배열을 사용할 필요 없이, 일차원 배열의 각 행에 퀸을 배치할 열을 기록
# 백트래킹을 사용할 경우, 브루트포스와 달리 불필요한 재귀를 시행하지 않기 때문에 O(N!)

N = int(input())
row = [0] * N
result = 0

def is_valid(x):
    for i in range(x):
        # 현재 행(x) 이전에 같은 값이 저장되어있다면 열 중복
        # 행 값의 차와 열 값의 차가 같다면 대각선 중복
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
        
    return True

def solution(x):
    global result

    if x == N:
        result += 1
        
    else:
        # 각 행에 퀸 배치
        for i in range(N):
            row[x] = i
            
            # 열, 대각선 확인
            # true 반환시 다음 행 확인
            if is_valid(x):
                solution(x + 1)

solution(0)
print(result)