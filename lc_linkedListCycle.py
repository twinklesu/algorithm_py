# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if head:
            visited = set()
            thisNode = head
            visited.add(hash(thisNode))
            while thisNode.next:
                if hash(thisNode.next) in visited:
                    return True
                thisNode = thisNode.next
                visited.add(hash(thisNode))
        return False