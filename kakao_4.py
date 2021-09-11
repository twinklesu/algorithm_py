def solution(n, info):
    global answer
    answer = [-1]

    # knapsack
    knapsack = [[0 for _ in range(n + 1)] for _ in range(12)]
    arrow = dict()
    for i, a, v in zip(range(1, 12), info, range(10, -1, -1)):
        arrow[i] = [a + 1, v]

    path = dict()
    for i in range(1, 12):
        for j in range(n + 1):
            if j - arrow[i][0] >= 0 and knapsack[i - 1][j] < arrow[i][1] + knapsack[i - 1][j - arrow[i][0]]:
                knapsack[i][j] = arrow[i][1] + knapsack[i - 1][j - arrow[i][0]]
                if (i - 1, j - arrow[i][0]) in path:
                    path[(i, j)] = path[(i - 1, j - arrow[i][0])] + [arrow[i][0]]
                else:
                    path[(i, j)] = [arrow[i][0]]

            elif knapsack[i - 1][j] >= arrow[i][1] + knapsack[i - 1][j - arrow[i][0]]:
                knapsack[i][j] = knapsack[i - 1][j]
                if (i - 1, j) in path:
                    path[(i, j)] = path[(i - 1, j)] + [0]
                else:
                    path[(i, j)] = [arrow[i][0]]

            else:
                if (i - 1, j) in path:
                    path[(i, j)] = path[(i - 1, j)] + [0]
                else:
                    path[(i, j)] = [0]
    diff = 0
    for p in path.values():
        p += [0] * (11 - len(p))
        p[-1] += n - sum(p)
        l_score = 0
        a_score = 0
        for l, a, s in zip(p, info, range(10, -1, -1)):
            if a >= l and s != 0 and a != 0:
                a_score += s
            elif l > a and s != 0 and l != 0:
                l_score += s
        if l_score - a_score >= diff:
            diff = l_score - a_score
            answer = p

    return answer