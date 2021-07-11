def dfs(numbers:list, perm: list, n:int, lenPerm:int):
    global maxAns
    if lenPerm == n:
        ans = 0
        for i in range(1, n):
            ans += abs(perm[i-1]-perm[i])
        maxAns = max(maxAns, ans)
    lenPerm += 1
    for num in numbers:
        if num not in perm:
            dfs(numbers, perm+[num], n, lenPerm)

def main():
    global maxAns
    maxAns = 0
    n = int(input())
    numbers = list(map(int, input().split()))

    dfs(numbers, [], n, 0)
    print(maxAns)


main()