import sys
input = sys.stdin.readline
INF = int(1e9)


def getTeamStats(team, stats):
    total = 0
    for player in team:
        for coplayer in team:
            total += stats[player][coplayer]
    return total


def recursion(home, n, k, stats):
    # 홈팀의 인원수가 전체의 절반, 즉 홈팀 구성이 끝나면 어웨이팀 자동 구성
    if len(home) == (n//2):
        away = [x for x in range(n) if x not in home]
        return abs(getTeamStats(home, stats)-getTeamStats(away, stats))
    elif n == k: # 없는 인덱스.
        return INF
    else:
        minimum = INF
        home.append(k)
        minimum = min(minimum, recursion(home, n, k+1, stats))
        home.remove(k)
        minimum = min(minimum, recursion(home, n, k+1, stats))
        return minimum


def main():
    n = int(input())
    stats = [list(map(int, input().rstrip().split())) for _ in range(n)]
    print(recursion([0], n, 1, stats)) # 홈팀엔 항상 0 포함. 어차피 상관없으니까


main()