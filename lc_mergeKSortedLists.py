from heapq import heappop, heappush
from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    dic = defaultdict(list)
    for thisNode in lists:
        if thisNode:
            # lists = [[]]일 때 걸러내기
            while thisNode.next is not None:
                dic[thisNode.val].append(thisNode)
                thisNode = thisNode.next
            dic[thisNode.val].append(thisNode)  # 마지막 node
    # dict에서 빼서 정렬된 리스트로 만들기
    sortedList = []
    for key in sorted(dic.keys()):
        for el in dic[key]:
            sortedList.append(el)
    # 리스트에 담긴 순으로 노드 연결
    headNode = None
    for ind, el in enumerate(sortedList):
        if ind != len(sortedList) - 1:
            el.next = sortedList[ind + 1]
        if ind == 0:
            headNode = el
    return headNode

# heapq 썼는데 실패

# def mergeKLists(self, lists):
#     heap = []
#     for thisNode in lists:
#         while thisNode.next is not None:
#             heappush(heap, [thisNode.val, thisNode])  # val로 힙정렬
#             thisNode = thisNode.next
#         heappush(heap, [thisNode.val, thisNode])  # 마지막 node
#     # 팝
#     isHead = True
#     headNode = ListNode()
#     while heap:
#         priority, thisNode = heappop(heap)
#         if isHead:
#             # 최초에만 들어와 headNode 설정
#             headNode = thisNode
#             isHead = False
#         if heap:
#             nextPriority, nextNode = heappop(heap)
#             thisNode.next = nextNode
#             heappush([nextPriority, nextNode])
#     thisNode.next = None  # 마지막 노드
#     return headNode
