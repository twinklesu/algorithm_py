n, score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    rank = list(map(int, input().split()))
    if n == p and score <= rank[-1]:
        print(-1)
    else:
        for ind, el in enumerate(rank):
            if el <= score:
                print(ind+1)
                break
        else:
            print(n+1)
