# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        global maxi
        maxi = -1001
        recursion(root)
        return maxi


def recursion(root):
    global maxi
    leftTree, rightTree = 0, 0

    if root.left:
        leftTree = recursion(root.left)
    if root.right:
        rightTree = recursion(root.right)

    pathSum = [root.val]
    pathSum.append(leftTree + root.val)  # left+root
    pathSum.append(rightTree + root.val)  # right+root
    pathSum.append(leftTree + rightTree + root.val)  # left + right + root

    maxi = max(maxi, max(pathSum))
    return max(pathSum[:3])

