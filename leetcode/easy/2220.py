# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num = start ^ goal
        div = num
        cnt = 0

        while(True):
            if(div < 1):
                break

            div, mod = divmod(div, 2)

            # 비트값(mod)가 1이 나올 때마다 cnt 증가
            if(mod == 1):
                cnt += 1

        return cnt

# start와 goal의 각 비트가 다른 횟수만큼 비트 플립이 필요
# 즉, XOR 연산 결과값 중 비트값이 1인 자릿수와 같음