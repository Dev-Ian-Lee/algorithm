# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

from typing import List

# n의 최대값이 2000이기 때문에 bruteforce 사용 시 시간 초과
# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         n = len(boxes)
#         ans = [0] * n

#         for i in range(n):
#             for j in range(n):
#                 if(i == j):
#                     continue

#                 if(boxes[j] == "1"):
#                     ans[i] += abs(i - j)

#         return ans

# 값이 1인 자리의 인덱스만 indices에 저장해 사용
# 통과는 했지만, 시간복잡도는 여전히 O(n^2)
# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         n = len(boxes)
#         ans = [0] * n
#         indices = []

#         for i in range(n):
#             if(boxes[i] == "1"):
#                 indices.append(i)

#         for i in range(n):
#             for j in range(indices):
#                 ans[i] += abs(i - j)

#         return ans

# 시간복잡도 : O(n)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        # leftCount : 각 인덱스보다 왼쪽에 있는 1의 개수
        # leftCount : 각 인덱스보다 왼쪽에 있는 1을 옮기기 위한 비용(칸 수)
        # rightCount : 각 인덱스보다 오른쪽에 있는 1의 개수
        # rightCount : 각 인덱스보다 오른쪽에 있는 1을 옮기기 위한 비용(칸 수)
        leftCount, leftCost, rightCount, rightCost = 0, 0, 0, 0

        for i in range(1, n):

            # 이전 인덱스가 1이라면 leftCount가 1증가하고, 0이면 이전 인덱스와 같은 값 유지
            if(boxes[i - 1] == "1"):
                leftCount += 1

            # 1을 오른쪽으로 한 칸 옮기기 위한 비용은, 왼쪽 1의 개수(leftCount)만큼 증가
            leftCost += leftCount
            ans[i] = leftCost

        for i in range(n - 2, -1, -1):
            if(boxes[i + 1] == "1"):
                rightCount += 1

            rightCost += rightCount

            # 각 자리의 정답은 leftCost와 rightCost를 합한 값
            ans[i] += rightCost

        return ans