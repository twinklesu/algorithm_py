# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def recursion(thisNode):
            if thisNode:
                li.append(str(thisNode.val))
                recursion(thisNode.left)
                recursion(thisNode.right)
            else:
                li.append("#")

        li = []
        recursion(root)
        return ",".join(li)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        global pointer
        pointer = 0
        li = list(map(str, data.split(",")))

        def recursion():
            global pointer
            if li[pointer] == "#":
                pointer += 1
                return None
            node = TreeNode(int(li[pointer]))
            pointer += 1
            node.left = recursion()
            node.right = recursion()
            return node

        return recursion()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))