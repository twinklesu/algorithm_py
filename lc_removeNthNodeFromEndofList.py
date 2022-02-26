# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        global count
        count = 0
        return recursion(head, n)


def recursion(thisNode, n):
    global count
    if thisNode.next is None:
        # 꼬리
        count += 1
        if count == n:
            return thisNode.next  # 꼬리가 삭제되는 경우
        return thisNode

    nextNode = recursion(thisNode.next, n)  # 바뀐게 return 될 경우
    # 꼬리에 닿고 나서 오는 부분
    count += 1
    if count < n:
        return thisNode
    elif count == n:
        return thisNode.next  # 이번 노드 삭제
    elif count == n + 1:
        thisNode.next = nextNode  # 이전 노드가 삭제된 경우
        return thisNode
    else:
        return thisNode