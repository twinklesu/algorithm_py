from collections import deque
from copy import copy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            ans = []
            q = deque()
            newQ = deque()
            newQ.append(root)
            while newQ:
                q = copy(newQ)
                newQ.clear()
                li = []
                while q:
                    thisNode = q.popleft()
                    if thisNode.left:
                        newQ.append(thisNode.left)
                    if thisNode.right:
                        newQ.append(thisNode.right)
                    li.append(thisNode.val)
                ans.append(li)
            return ans

        else:
            return []

