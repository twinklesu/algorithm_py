from collections import defaultdict
from math import sqrt, ceil


def shieve(n):
    isPrime = {i: True for i in range(n + 1)}
    isPrime[1] = False
    for i in range(2, ceil(sqrt(n)) + 1):
        if isPrime[i]:
            for j in range(i + i, n + 1, i):
                isPrime[j] = False
    return isPrime


def solution(n, k):
    answer = 0
    candidate = defaultdict(int)

    num = 0
    count = 0
    maxi = 0

    while n > 0:
        n, q = n // k, n % k
        if q != 0:
            num += q * 10 ** count
            count += 1
        elif num != 0:
            candidate[num] += 1
            if num > maxi:
                maxi = num
            num = 0
            count = 0
    if num != 0:
        candidate[num] += 1
        if num > maxi:
            maxi = num

    isPrime = shieve(maxi)

    for c in candidate:
        if isPrime[c]:
            answer += candidate[c]

    return answer