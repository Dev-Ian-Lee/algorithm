# https://leetcode.com/problems/decode-xored-array/

from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret = [first]
        
        for i in range(len(encoded)):
            ret.append(encoded[i]^ret[i])
            
        return ret