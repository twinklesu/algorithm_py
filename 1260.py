from collections import defaultdict, deque


def dfs(graph: defaultdict, v: int, beenTo: list):
    if v in beenTo:
        return
    beenTo.append(v)
    v_value = graph[v]
    v_value.sort()
    for nextNode in v_value:
        dfs(graph, nextNode, beenTo)



def bfs(graph: defaultdict, v:int, beenTo: list):
    beenTo.append(v)
    v_value = graph[v]
    v_value.sort()
    waitingQ = deque(v_value)
    while waitingQ:
        temp = waitingQ.popleft()
        beenTo.append(temp)
        new_value = graph[temp]
        new_value.sort()
        for value in new_value:
            if value not in beenTo and value not in waitingQ:
                waitingQ.append(value)


def main():
    n,m,v = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        key, value = map(int, input().split())
        graph[key].append(value)
        graph[value].append(key)

    dfsAns = []
    dfs(graph, v, dfsAns)
    print(*dfsAns)

    bfsAns = []
    bfs(graph, v, bfsAns)
    print(*bfsAns)


main()
