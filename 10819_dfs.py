def dfs(numbers:list, perm: list, n:int, lenPerm:int):
    global maxAns
    if lenPerm == n:
        ans = 0
        beforeNum = numbers[perm[0]]
        for i in perm[1:]:
            ans += abs(beforeNum-numbers[i])
            beforeNum = numbers[i]
        maxAns = max(maxAns, ans)
    lenPerm += 1
    for ind in range(n):
        if ind not in perm:
            dfs(numbers, perm+[ind], n, lenPerm)

def main():
    global maxAns
    maxAns = 0
    n = int(input())
    numbers = list(map(int, input().split()))

    dfs(numbers, [], n, 0)
    print(maxAns)


main()