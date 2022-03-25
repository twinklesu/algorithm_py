# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            rootVal = preorder[0] # root 찾기
            rootIndex = inorder.index(rootVal) # 좌 우 나눌 인덱스
            root = TreeNode(rootVal)
            root.left = self.buildTree(preorder[1:1+rootIndex], inorder[:rootIndex]) # 왼쪽 subTree
            root.right = self.buildTree(preorder[1+rootIndex:], inorder[rootIndex+1:]) # 오른쪽 subTree
            return root
        else:
            return None