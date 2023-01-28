# <이것이 취업을 위한 코딩 테스트다> 예제 4-2

# 초기 코드
# N = int(input())

# count = 0
# hour = 0
# minute = 0
# second = 0

# while(True):
#     second += 1

#     if second == 60:
#         second = 0
#         minute += 1

#     if minute == 60:
#         minute = 0
#         hour += 1

#     if '3' in str(hour) + str(minute) + str(second):
#         count += 1

#     if hour == N and minute == 59 and second == 59:
#         break

# print(count)

# 개선 코드
N = int(input())

count = 0
for hour in range(N + 1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                count += 1

print(count)