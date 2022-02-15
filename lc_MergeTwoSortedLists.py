# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def mergeTwoLists(list1, list2):
    baseList = list1 if list1.val < list2.val else list2
    insertingList = list2 if list1.val < list2.val else list1

    head = baseList

    while insertingList and baseList.next:
        if baseList.val <= insertingList.val <= baseList.next.val:
            insertingNode = insertingList
            insertingList = insertingList.next

            insertingNode.next = baseList.next  # 뒷 부분 연결
            baseList.next = insertingNode  # 앞부분 연결
            baseList = baseList.next
        else:
            baseList = baseList.next

    # 마지막 연결
    if insertingList:
        # baseList.next == None 인데 while 이 종료
        baseList.next = insertingList


    return head


node11 = ListNode(1)
node12 = ListNode(2)
node13 = ListNode(3)
node11.next = node12
node12.next = node13

node21 = ListNode(2)
node22 = ListNode(5)
node23 = ListNode(6)
node21.next = node22
node22.next = node23
mergeTwoLists(node21, node11)