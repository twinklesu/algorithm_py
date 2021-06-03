import sys
input = sys.stdin.readline


def getDivisor(n):
    ans = set()
    for i in range(1, n//2+1):
        if n%i == 0:
            ans.add(i)
            ans.add(n//i)
    return ans


def solution():
    numbers = list(map(int, input().rstrip().split()))
    n = numbers[0]
    divisor = [None]
    for num in numbers[1:]:
        divisor.append(getDivisor(num))

    summedGcd = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            gcd = max(divisor[i].intersection(divisor[j]))
            summedGcd += gcd
    print(summedGcd)


def main():
    t = int(input())
    for _ in range(t):
        solution()


main()
