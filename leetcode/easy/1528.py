# https://leetcode.com/problems/shuffle-string/

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        ls = [0] * n
        ret = ""

        for i in range(n):
            ls[indices[i]] = s[i]

        for ele in ls:
            ret += ele
            
        return ret