n, m = map(int, input().split())
prices=[]

for _ in range(m):
    prices.append(int(input()))

prices.sort(reverse=True)

price = 0
revenue = 0

for i in range(0,min(n,m)):
    a = prices[i]
    rev = a*(i+1)
    if rev > revenue:
        revenue = rev
        price = a

print(price, revenue)
