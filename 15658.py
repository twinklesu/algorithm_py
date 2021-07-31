def recursion(numbers, operationNum, n, perm):
    global minAns, maxAns
    if len(perm) == n-1:
        ans = numbers[0]
        for num, op in zip(numbers[1:], perm):
            if op == 0:
                ans += num
            elif op == 1:
                ans -= num
            elif op == 2:
                ans *= num
            else:
                if ans < 0:
                    ans = -(abs(ans) // num)
                else:
                    ans //= num
        minAns = min(minAns, ans)
        maxAns = max(maxAns, ans)
        return
    for ind, el in enumerate(operationNum):
        if el != 0:
            operationNum[ind] -= 1
            recursion(numbers, operationNum, n, perm + [ind])
            operationNum[ind] += 1


def main():
    global minAns, maxAns

    n = int(input())
    numbers = list(map(int, input().split()))
    operationNum = list(map(int, input().split()))

    minAns = 10**9+1
    maxAns = -10**9-1

    recursion(numbers, operationNum, n, [])

    print(maxAns, minAns, sep='\n')


main()
