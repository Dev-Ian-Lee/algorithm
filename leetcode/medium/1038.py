# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def recur(node, acc):

            # 탐색 종료 시, 현재까지의 노드값 합 반환
            if(not node):
                return acc

            # 오른쪽 서브트리 탐색해 합한 값을 현재 노드값에 더함
            node.val += recur(node.right, acc)

            # 오른쪽 탐색 종료 이후, 왼쪽 탐색
            # 이때, node.val에는 오른쪽 탐색한 값이 반영되어 있음
            return recur(node.left, node.val)

        recur(root, 0)
        return root