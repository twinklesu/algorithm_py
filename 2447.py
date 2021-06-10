def recursion(n: int, x: int, y: int, pattern: list):
    if n == 1:
        return

    n//=3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                for k in range(n):
                    pattern[x+n+k][y+n:y+2*n] = [' ']*n
            recursion(n, x+i*n, y+j*n, pattern)

def main():
    n = int(input())
    pattern = [['*' for _ in range(n)] for _ in range(n)]
    recursion(n, 0, 0, pattern)
    for p in pattern:
        print(''.join(p))


main()