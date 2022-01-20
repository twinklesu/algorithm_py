# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(root):
    global maxDepth
    if root:
        maxDepth = 1
        solution(root, 1)
        return maxDepth
    else:
        return 0


def solution(thisNode, depth):
    global maxDepth
    if thisNode.left is None and thisNode.right is None:
        maxDepth = max(maxDepth, depth)
        return
    if thisNode.left:
        solution(thisNode.left, depth + 1)
    if thisNode.right:
        solution(thisNode.right, depth + 1)