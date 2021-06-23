def solution():
    n = int(input())
    numbers = [[] for _ in range(2)]
    for i in range(2):
        numbers[i] = list(map(int, input().split()))

    numbers[0][1] += numbers[1][0]
    numbers[1][1] += numbers[0][0]
    for i in range(2, n):
        numbers[0][i] += max(numbers[1][i-1], numbers[1][i-2])
        numbers[1][i] += max(numbers[0][i-1], numbers[0][i-2])

    print(max(numbers[0][-1], numbers[1][-1]))


def main():
    t = int(input())
    for _ in range(t):
        solution()


main()