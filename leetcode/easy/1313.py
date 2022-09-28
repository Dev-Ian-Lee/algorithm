# https://leetcode.com/problems/decompress-run-length-encoded-list/

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        ret = []

        while(True):
            if(i >= len(nums) - 1):
                break

            for _ in range(nums[i]):
                ret.append(nums[i + 1])

            i += 2

        return ret