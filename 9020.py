def solution(primeNumbers: list, end):
    n = int(input())
    start_limit = n//2
    start = 0
    end -= 1
    ans = []

    while primeNumbers[start] <= start_limit:
        summed = primeNumbers[start] + primeNumbers[end]
        if summed > n:
            end -= 1
        elif summed == n:
            ans = [start, end]
            start += 1
            end -= 1
        else:
            start += 1

    print(primeNumbers[ans[0]], primeNumbers[ans[1]])


def main():
    # 소수 먼저 구하기
    isPrimeList = [True for _ in range(10001)]
    for i in range(2, 101):
        if isPrimeList[i]:
            for j in range(i+i, 10001, i):
                isPrimeList[j] = False
    primeNumbers = []
    for isPrime, num in zip(isPrimeList[2:], range(2, 10001)):
        if isPrime:
            primeNumbers.append(num)
    numOfPrimes = len(primeNumbers)

    t = int(input())
    for _ in range(t):
        solution(primeNumbers, numOfPrimes)


main()
