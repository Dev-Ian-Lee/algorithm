# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

from typing import List

# 시간복잡도 : O(n^2)
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        max_c_ls = []
        
        for i in range(n):
            max_r = max(grid[i])
            max_c = 0

            for j in range(n):
                
                # 행의 최대값과 각 수와의 차이
                matrix[i][j] = max_r - grid[i][j]

                # 각 열의 최대값 구해 리스트에 저장
                if(grid[j][i] > max_c):
                    max_c = grid[j][i]  

            max_c_ls.append(max_c)
        
        for i in range(n):
            for j in range(n):
                # 행의 최대값과 각 수와의 차이, 열의 최대값과 각 수의 차이 중 작은 것 저장
                matrix[i][j] = min(matrix[i][j], max_c_ls[j] - grid[i][j])

        ret = 0
        for i in range(n):
            ret += sum(matrix[i])

        return ret