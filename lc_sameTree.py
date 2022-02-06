from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q) -> bool:
    q1 = deque()
    q2 = deque()

    if p and q:
        q1.append(p)
        q2.append(q)
        while q1 and q2:
            thisNode1 = q1.popleft()
            thisNode2 = q2.popleft()
            if thisNode1 and thisNode2:
                if thisNode1.val == thisNode2.val:
                    q1.append(thisNode1.left)
                    q1.append(thisNode1.right)
                    q2.append(thisNode2.left)
                    q2.append(thisNode2.right)
                else:
                    # same location, but diff. value
                    return False
            elif not thisNode1 and not thisNode2:
                # both are empty node
                pass
            else:
                # one of them is empty, and another is not
                return False
        if not q1 and not q2:
            # if both Q empty and done
            return True
        else:
            # one of them has left value
            return False
    elif not p and not q:
        # both are same due to empty
        return True
    else:
        # one of them is empty, and another is not
        return False


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
one.left = two
one.right = three
print(isSameTree(one, one))