# https://www.acmicpc.net/problem/13335

# 시간복잡도: O(N)
# 최대 경우의 수(n * w)가 100,000이므로 O(N)에 해결 가능
# pop() 연산을 자주 사용하기 때문에 pop() 연산의 시간복잡도가 O(1)인 deque 사용

from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

# 현재 다리 상태, 다리 위에 있는 트럭이 이동한 거리
bridge = deque()
dist = deque()

total_time = 0
truck_idx = 0

while True:
    # 다리 위에 남은 트럭이 없고, 모든 트럭을 다 고려했을 경우 break
    if len(bridge) == 0 and truck_idx == len(trucks):
        break
        
    # 맨 처음에 있는 트럭이 다리를 모두 지난 경우, bridge에서 제거
    if len(dist) > 0 and dist[0] >= w:
        bridge.popleft()
        dist.popleft()
    
    # 다리에 하나의 트럭이 더 올라가도 최대하중을 넘지 않는 경우, bridge에 추가
    if truck_idx < len(trucks) and sum(bridge) + trucks[truck_idx] <= L:
        bridge.append(trucks[truck_idx])
        dist.append(0)
        truck_idx += 1
    
    # 매 반복마다 트럭 이동 거리, 단위시간 증가
    dist = deque([ele + 1 for ele in dist])
    total_time += 1

print(total_time)