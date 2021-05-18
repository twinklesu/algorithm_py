from collections import deque


def solution():
    n, m = map(int, input().split())
    que = deque()
    priority = list(map(int, input().split()))
    for i, j in zip(range(n), priority):
        que.append([i, j])

    count = 1
    while True:
        temp = que.popleft()
        ind = temp[0]
        pri = temp[1]
        if ind == m and pri == max(priority):
            print(count)
            break
        elif ind != m and pri == max(priority):
            priority.remove(pri)
            count += 1
        else:
            que.append(temp)





def main():
    n = int(input())
    for _ in range(n):
        solution()


main()