# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s_left, s_right = s.split(":")
        
        alps = []
        alps_diff = ord(s_right[0]) - ord(s_left[0])
        for i in range(alps_diff + 1):
            alps.append(chr(ord(s_left[0]) + i))
        
        nums = []
        nums_diff = ord(s_right[1]) - ord(s_left[1])
        for i in range(nums_diff + 1):
            nums.append(chr(ord(s_left[1]) + i))
        
        ret = []
        
        for alp in alps:
            for num in nums:
                ret.append(alp + num)
                
        return ret

# 파이썬에서 유니코드 구할 때는 ord(), 유니코드를 문자로 변환할 때는 chr() 사용