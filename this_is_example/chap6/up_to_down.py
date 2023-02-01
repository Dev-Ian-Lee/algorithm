# <이것이 취업을 위한 코딩 테스트다> 실전 문제 6-7

N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort(reverse = True)

for ele in nums:
    print(ele, end = ' ')

print()