# https://www.acmicpc.net/problem/1931

n = int(input())

meetings = []
for i in range(n):
    meetings.append(list(map(int, input().split())))

# 종료 시간 순으로 정렬
# 종료 시간이 같을 경우, 시작 시간 순으로 정렬
meetings.sort(key = lambda x : (x[1], x[0]))

cnt = 1
end_time = meetings[0][1]

# 순차적으로 탐색해 현재 회의의 종료 시간 이후에 시작하는 회의를 진행
for meeting in meetings[1:]:
    if meeting[0] >= end_time:
        cnt += 1
        end_time = meeting[1]

print(cnt)