# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        li = []
        thisNode = head
        while thisNode.next:
            li.append(thisNode)
            thisNode = thisNode.next
        li.append(thisNode)

        N = len(li)
        insertPoint = 0
        for i in range(N - 1, N // 2, -1):
            li[insertPoint].next = li[i]
            li[i].next = li[insertPoint + 1]
            insertPoint += 1

        li[N // 2].next = None