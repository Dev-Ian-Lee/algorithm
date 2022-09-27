# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

from typing import List

# bruteforce -> 시간복잡도 O(n^2)
class Solution:
    def euclidean_dist(self, x1, y1, x2, y2):
        return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        
        for query in queries:
            cnt = 0
        
            x, y, r = query
            
            # 원 중심과 point의 유클리드 거리가 반지름보다 같거나 작을 경우, cnt 증가
            for point in points:
                if(self.euclidean_dist(x, y, point[0], point[1]) <= r):
                    cnt += 1
                    
            answer.append(cnt)
            
        return answer

# sort, binary search -> 시간복잡도 O(nlogn) (실패, 나중에 다시)
# class Solution:
#     def euclidean_dist(self, x1, y1, x2, y2):
#         return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    
#     def binary_search(self, points, query):
#         start = 0
#         end = len(points) - 1
#         mid = (start + end) // 2

#         x, y, r = query
#         x2, y2 = points[mid][0], points[mid][1]

#         while(True):
#             mid = (start + end) // 2

#             if(start > end):
#                 break

#             if(self.euclidean_dist(x, y, x2, y2) > r):
#                 end = mid - 1

#             elif(self.euclidean_dist(x, y, x2, y2) <= r):
#                 start = mid + 1

#         return mid + 1

#     def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
#         points.sort()
#         answer = []
        
#         for query in queries:
#             cnt = self.binary_search(points, query)

#             answer.append(cnt)
        
#         return answer