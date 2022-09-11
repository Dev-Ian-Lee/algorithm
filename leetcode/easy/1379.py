# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # 리스트 스택처럼 사용
        stack = []
        stack.append((original, cloned))

        while stack:
            org, clone = stack.pop()

            # target에 도착하면 clone 반환
            if(org == target):
                return clone

            # 왼쪽 자식 트리 탐색
            if(org.left):
                stack.append((org.left, clone.left))

            # 오른쪽 자식 트리 탐색
            if(org.right):
                stack.append((org.right, clone.right))

# DFS 사용해서 트리 탐색
# original과 cloned 트리 동시 탐색