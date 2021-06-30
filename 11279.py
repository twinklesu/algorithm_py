from heapq import heappop, heappush
import sys
input = sys.stdin.readline



def myHeap():
    n = int(input())
    heap = []
    lenHeap = 0
    for _ in range(n):
        num = int(input())
        if num == 0:
            if heap:
                lenHeap -= 1
                print(heap[lenHeap])
                heap[lenHeap] = 2**31+1
            else:
                print(0)
        else:
            targetInd = lenHeap
            for ind, el in enumerate(heap):
                if num < el:
                    targetInd = ind
                    break
            heap = heap[:targetInd] + [num] + heap[targetInd:]
            lenHeap +=1

myHeap()

def libraryHeap():
    n = int(input())
    heap = []
    for _ in range(n):
        num = int(input())
        if num == 0:
            if heap:
                print(heappop(heap)[1])
            else:
                print(0)
        else:
            heappush(heap, [-num, num])


