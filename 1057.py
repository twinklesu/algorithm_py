n, jimin, hansoo = map(int, input().split())

p = min(jimin, hansoo)
q = max(jimin, hansoo)

def newNumber(n):
    if n%2 == 0:
        return n//2
    else:
        return (n+1)//2

round = 0
people = list(range(n+1)) # 0은 자리 채우고, 1~n
while people != [0]:
    round +=1
    if p%2 != 0 and p+1 == q:
        print(round)
        break
    p = newNumber(p)
    q = newNumber(q)
    people = list(range(newNumber(n)+1))
else:
    print(-1)
