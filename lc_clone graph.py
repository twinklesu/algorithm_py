
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    if node:
        graph = [[] for _ in range(101)]
        visited = [False for _ in range(101)]
        visited[0] = True  # place holder
        visited[node.val] = True
        stack = deque()
        stack.append(node)

        while stack:
            thisNode = stack.pop()
            for nextNode in thisNode.neighbors:
                graph[thisNode.val].append(nextNode.val)
                if not visited[nextNode.val]:
                    visited[nextNode.val] = True
                    stack.append(nextNode)

        maxVal = 0
        for ind, v in enumerate(visited):
            if not v:
                maxVal = ind - 1
                break

        # new node generation
        nodes = [None]  # place holder
        for i in range(1, maxVal + 1):
            nodes.append(Node(val=i))

        headNode = nodes[1]
        for i in range(1, maxVal+1):
            for nn in graph[i]:
                nodes[i].neighbors.append(nodes[nn])
        return headNode

    else:
        return None

one = Node(1)
two = Node(2)
three=Node(3)
four = Node(4)
one.neighbors = [two]
two.neighbors = [one, three]
three.neighbors = [two, four]
four.neighbors = [three]
# one = Node(1)
#
# one = Node(1)
# two = Node(2)
# one.neighbors = [two]
# two.neighbors = [one]
answer = cloneGraph(one)
