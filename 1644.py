from math import sqrt, ceil

def shieve(n):
    isPrime = [True for _ in range(n+1)]
    for i in range(2, ceil(sqrt(n))):
        if isPrime[i]:
            for j in range(i+i, n+1, i):
                isPrime[j] = False
    primeNum = []
    for i in range(2, n+1):
        if isPrime[i]:
            primeNum.append(i)
    return primeNum


def solution():
    n = int(input())
    primeNum = shieve(n)
    lenP = len(primeNum)
    start = 0
    end = 1
    count = 0
    while start < end <= lenP:
        if sum(primeNum[start:end]) < n:
            end += 1
        elif sum(primeNum[start:end]) > n:
            start += 1
        else:
            count += 1
            start += 1
            end += 1
    print(count)


solution()