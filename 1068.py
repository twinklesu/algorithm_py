from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
inline = list(map(int, input().split()))
tree = defaultdict(list)
delete = int(input())
for u, v in enumerate(inline):
    if u == delete:
        continue
    tree[v].append(u)

# 백트래킹 dfs
count = 0
stack = deque()
if -1 in tree:
    stack.append(tree[-1][0])
    while stack:
        thisNode = stack.pop()
        if thisNode in tree:
            for nextNode in tree[thisNode]:
                stack.append(nextNode)
        else:
            count += 1

print(count)
