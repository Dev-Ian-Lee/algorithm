# <이것이 취업을 위한 코딩 테스트다> 실전 문제 6-8

N = int(input())

students = []
for _ in range(N):
    name, score = input().split()
    students.append([name, int(score)])

arr = sorted(students, key = lambda x : x[1])

for ele in arr:
    print(ele[0], end = ' ')

print()