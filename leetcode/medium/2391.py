# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/

from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        types = ["M", "P", "G"]
        time = 0
        travel.insert(0, 0)
        last_idx = 0

        for t in types:
            
            # 각 타입의 트럭이 있었던 마지막 인덱스
            last_idx = 0
            for i in range(len(garbage)):

                # 집에 해당하는 타입의 쓰레기가 있고 첫 집이 아닐 경우,
                if(t in garbage[i] and i != 0):

                    # 이동 시간 계산 및 마지막 인덱스 현재 위치로 갱신
                    time += sum(travel[last_idx + 1 : i + 1])
                    last_idx = i

                # 집의 쓰레기를 하나씩 검사해 수거하는데 걸리는 시간 계산
                for c in garbage[i]:
                    if(c == t):
                        time += 1

        return time