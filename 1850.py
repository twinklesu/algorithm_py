def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def main():
    aStr, bStr = map(str, input().split())
    lenA = len(aStr)
    lenB = len(bStr)
    n = max(lenA, lenB)
    aStr = '0'*(n-lenA) + aStr
    bStr = '0'*(n-lenB) + bStr

    a = list(map(int, aStr))
    b = list(map(int, bStr))
    for i in range(n):
        a[i] = a[i]-b[i]
    sub = 0
    for s in a:
        sub *= 10
        sub += s
    sub = abs(sub)
    print('1'*sub)


main()