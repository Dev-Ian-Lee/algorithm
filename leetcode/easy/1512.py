# https://leetcode.com/problems/number-of-good-pairs/

from typing import List

# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         cnt = 0
        
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if(nums[i] == nums[j]):
#                     cnt += 1
                    
#         return cnt
        

# HashMap(dictionary) 사용해 시간복잡도 개선(O(n^2) -> O(n))
# dictionary에 대한 in 연산자의 시간복잡도는 O(1)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counted_times = {}
        cnt = 0
        
        for num in nums:
            if(num in counted_times.keys()):
                cnt += counted_times[num]
                counted_times[num] += 1

            else:
                counted_times[num] = 1

        return cnt

# 같은 숫자가 기존에 n개 있을 때 해당 숫자가 한 번 더 들어오면,
# 만들 수 있는 조합의 수 = (기존 조합의 개수 + n)
# 새로 들어온 숫자와 기존 숫자 n개를 한 번씩 조합 가능하기 때문