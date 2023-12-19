# https://www.acmicpc.net/problem/15666

# 걸린 시간: 15min
# 시간복잡도: O(N^M)

# 비내림차순, 즉 같거나 큰 순으로 정렬해야하기 때문에 조합
# 같은 수를 여러 번 사용할 수 있기 때문에 중복조합(combinations with replacement)
# 중복조합의 시간복잡도가 O(N^M)

from itertools import combinations_with_replacement

N, M = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()

# set을 사용해 중복 수열 제거
s = set()
for ele in combinations_with_replacement(ls, M):
    s.add(ele)

# 오름차순 정렬을 위해 리스트로 변경해 출력
s_to_list = list(s)
s_to_list.sort()
for ele in s_to_list:
    for num in ele:
        print(num, end = " ")
        
    print()