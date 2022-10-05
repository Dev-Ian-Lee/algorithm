# https://leetcode.com/problems/deepest-leaves-sum/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root):
        self.ans = 0
        self.depth = 0

        # 가장 깊은 서브트리 탐색
        def find_deepest_leaves(node):
            if(not node): 
                return 0

            # 왼쪽과 오른쪽 서브트리 중 더 큰 레벨 + 1(현재 노드 포함)이 현재 노드의 레벨
            return max(find_deepest_leaves(node.left), find_deepest_leaves(node.right)) + 1
        
        # 가장 깊은 리프 노드의 합 계산
        def deepest_leaves_sum(node, d):
            if(not node): 
                return

            # 가장 깊은 리프 노드의 값 축적
            if(d == self.depth): 
                self.ans += node.val

            deepest_leaves_sum(node.left, d + 1)
            deepest_leaves_sum(node.right, d + 1)
    
        self.depth = find_deepest_leaves(root)
        deepest_leaves_sum(root, 1)

        return self.ans