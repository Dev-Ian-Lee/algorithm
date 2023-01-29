# <이것이 취업을 위한 코딩 테스트다> 예제 5-1

from collections import deque

queue = deque()

# 삽입 연산은 append(), 삭제 연산은 popleft()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)

# 역순으로 변경
queue.reverse()
print(queue)