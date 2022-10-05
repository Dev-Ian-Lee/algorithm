# https://leetcode.com/problems/xor-operation-in-an-array/description/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n
        ret = start

        for i in range(n):
            nums[i] = start + 2 * i

        for i in range(1, n):
            ret = ret ^ nums[i]

        return ret