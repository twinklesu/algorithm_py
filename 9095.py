num = {1:1, 2:2, 3:4}


def sol():
    n = int(input())
    if n in num:
        print(num[n])
    else:
        for i in range(max(num)+1, n+1):
            num[i] = num[i-1] + num[i-2] + num[i-3]
        print(num[n])


def main():
    n = int(input())
    for _ in range(n):
        sol()

main()