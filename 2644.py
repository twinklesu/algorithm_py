import sys
input = sys.stdin.readline
from collections import defaultdict


def dfs(parent: int, child: int, count: int, parentToChild: defaultdict, visited: list):
    global globalCount
    if parent == child:
        globalCount = count
        return
    for c in parentToChild[parent]:
        if not visited[c]:
            visited[c] = True
            dfs(c, child, count+1, parentToChild, visited)


def main():
    global globalCount
    globalCount = 0

    n = int(input())
    one, two = map(int, input().split())
    m = int(input())
    parentToChild = defaultdict(list)
    childToParent = dict()
    for _ in range(m):
        parent, child = map(int, input().split())
        parentToChild[parent].append(child)
        childToParent[child] = parent
    # one 의 자식에 two가 있는지
    visited = [False for _ in range(n+1)]
    visited[0] = True
    visited[one] = True
    dfs(one, two, 0, parentToChild, visited)
    if globalCount != 0:
        print(globalCount)
        return
    # two 부터 root으로 가면서 자식에 one이 있는지. visited 확인
    visited = [False for _ in range(n+1)]
    visited[0] = True
    countUpFromTwo = 0
    while globalCount == 0:
        visited[two] = True
        dfs(two, one, countUpFromTwo, parentToChild, visited)
        if two in childToParent:
            two = childToParent[two] # 부모로 올라감
            countUpFromTwo += 1 # 1촌 올려서 시작
        else:
            break
    if globalCount != 0:
        print(globalCount)
    else:
        print(-1)


main()