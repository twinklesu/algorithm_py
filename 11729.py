def solution(n: int, start: int, end: int, ans: list):
    if n == 1:
        ans.append(str(start) + " " + str(end))
        return
    hanoi = {1, 2, 3}
    temp = hanoi - {start, end}
    temp = temp.pop()
    solution(n-1, start, temp, ans)
    ans.append(str(start) + " " + str(end))
    solution(n-1, temp, end, ans)
    return


def main():
    n = int(input())
    start = 1
    end = 3
    ans = []
    solution(n, start, end, ans)
    print(len(ans))
    for a in ans:
        print(a)


main()
