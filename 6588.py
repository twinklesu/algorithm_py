import sys
input = sys.stdin.readline

maxNum = 10**6
isPrime = [True for _ in range(maxNum+1)]
for i in range(2, 10**3+1):
    if isPrime[i]:
        for j in range(i+i, maxNum+1, i):
            isPrime[j] = False


while True:
    num = int(input())
    if num == 0:
        break
    pointer = 3
    while pointer < num:
        if isPrime[pointer] and isPrime[num-pointer]:
            # a and b both are prime number
            print(num, "=", pointer, "+", num-pointer)
            break
        else:
            pointer += 1
    else:
        print("Goldbach's conjecture is wrong.")