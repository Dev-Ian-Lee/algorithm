# https://www.acmicpc.net/problem/1927

# 걸린 시간: 10min
# 시간복잡도: O(N * logN)

# heapq 라이브러리 사용해 최소 힙 구현 가능
# heapify()는 반환값 없이 매개변수로 받은 리스트를 힙으로 변환함을 주의

import sys
from heapq import *

N = int(sys.stdin.readline().rstrip())

q = []
heapify(q)

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    
    if num == 0:
        if len(q) == 0:
            print(0)
            
        else:
            print(heappop(q))
        
        
    else:
        heappush(q, num)
