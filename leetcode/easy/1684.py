# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

from typing import List

# O(N^3)
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ls = set(allowed)
        ret = 0
        
        for word in words:
            cnt = 0

            for c in word:
                if(c in ls):
                    cnt += 1

            if(cnt == len(word)):
                ret += 1

        return ret