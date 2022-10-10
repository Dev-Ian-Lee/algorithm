# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        # preorder 리스트의 맨 처음 항목이 루트 노드
        root = TreeNode(preorder[0])
        stack = [root]

        for ele in preorder[1:]:
            node = TreeNode(ele)

            # 리스트의 값이 스택의 최상단 노드의 값보다 작을 경우, 왼쪽 자식
            if(ele < stack[-1].val):
                stack[-1].left = node
                
            # 클 경우, 리스트의 값보다 작은 값 중에서 가장 큰 값을 갖는 노드를 스택에서 추출
            # 추출된 노드가 부모가 되고, 리스트의 값이 더 크기 때문에 오른쪽 자식
            else:
                while stack and stack[-1].val < ele:
                    parent = stack.pop(-1)

                parent.right = node

            stack.append(node)

        return root