def primeSieve(n):
    isPrime = [True for _ in range(n+1)]

    m = int(n**0.5)
    for i in range(2, m+1):
        if isPrime[i]:
            for k in range(i+i, n+1, i):
                isPrime[k] = False
    return [i for i in range(n-1) if isPrime[i]]


def main():
    primeList = primeSieve(123456*2)
    n = int(input())
    while n != 0:
        count = 0
        for num in primeList:
            if num > n*2:
                break
            if num > n:
                count += 1
        print(count)
        n = int(input())


main()