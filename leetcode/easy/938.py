# https://leetcode.com/problems/range-sum-of-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ret = 0

        def dfs(node):
            if(not node):
                return 0

            if(low <= node.val <= high):
                self.ret += node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ret