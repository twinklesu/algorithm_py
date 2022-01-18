class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    if head:
        global newHead
        solution(head, True)
        return newHead
    else:
        return None


def solution(thisNode, isOriginalHead):
    global newHead
    if not thisNode.next:  # if None
        newHead = thisNode
        return newHead
    preNode = solution(thisNode.next, False)  # go down to tail
    preNode.next = thisNode  # when come up, reverse
    if isOriginalHead:
        thisNode.next = None
    return thisNode


nodeList = []
for i in range(1,6):
    nodeList.append(ListNode(i))
for ind, el in enumerate(nodeList):
    if ind == 4:
        el.next = None
    else:
        el.next = nodeList[ind+1]

reverseList(nodeList[0])