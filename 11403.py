import sys
input = sys.stdin.readline


def main():
    n = int(input())
    table = []
    for _ in range(n):
        line = list(map(int, input().rstrip().split()))
        table.append(line)

    # 0부터 n까지 거쳐갈 노드 순회
    for interNode in range(n):
        for start in range(n):
            for end in range(n):
                if table[start][end] == 0 and table[start][interNode] + table[interNode][end] > 1:
                    table[start][end] = 1

    for t in table:
        print(*t)


main()
