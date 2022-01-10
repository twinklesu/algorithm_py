
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        result = "val: "
        result += str(self.val)
        result += ", neighbors: "
        for n in self.neighbors:
            result += str(n.val)
            result += ", "
        return result


def cloneGraph(node: 'Node') -> 'Node':
    if node:
        nodeList = [Node(i) for i in range(101)]
        visited = [False for _ in range(101)]
        visited[0] = True  # place holder
        visited[node.val] = True
        stack = deque()
        stack.append(node)
        nodeList[node.val] = Node(node.val)

        while stack:
            thisNode = stack.pop()
            for nextNode in thisNode.neighbors:
                nodeList[thisNode.val].neighbors.append(nodeList[nextNode.val])
                if not visited[nextNode.val]:
                    visited[nextNode.val] = True
                    stack.append(nextNode)

        return nodeList[node.val]
    else:
        return None


one = Node(1)
two = Node(2)
three=Node(3)
four = Node(4)
one.neighbors = [two, four]
two.neighbors = [one, three]
three.neighbors = [two, four]
four.neighbors = [three, one]
# one = Node(1)
#
# one = Node(1)
# two = Node(2)
# one.neighbors = [two]
# two.neighbors = [one]
answer = cloneGraph(one)
stack = deque()
stack.append(answer)
visited = dict()

while stack:
    thisNode = stack.pop()
    print(thisNode)
    visited[thisNode.val] = True
    for nn in thisNode.neighbors:
        if nn.val not in visited:
            stack.append(nn)
