import sys
input = sys.stdin.readline


def gcd(a,b):
    while b != 0:
        d = a%b
        a,b = b,d
    return a


def solution():
    numbers = list(map(int, input().rstrip().split()))
    n = numbers[0]
    summedGcd = 0
    for i in range(1,n):
        for j in range(i+1, n+1):
            summedGcd += gcd(numbers[i], numbers[j])
    print(summedGcd)


def main():
    t = int(input())
    for _ in range(t):
        solution()

main()