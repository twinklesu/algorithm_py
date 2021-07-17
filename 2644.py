from collections import defaultdict, deque

# 트리가 아니라 양방향 그래프로 생각. 아무튼 찾아가기만 하면 되니까


def dfs(relation: dict, count: int, a: int, b: int):
    global globalCount
    if a == b:
        globalCount = count
        return
    if a in relation:
        nextNodes = relation.pop(a)
        for nn in nextNodes:
            dfs(relation, count+1, nn, b)


n = int(input())
a, b = map(int, input().split())
m = int(input())
relation = defaultdict(list)
for _ in range(m):
    p, q = map(int, input().split())
    relation[p].append(q)
    relation[q].append(p)
globalCount = -1
dfs(relation, 0, a, b)
print(globalCount)