n = int(input())
prices = list(map(int, input().split()))
prices = [0] + prices

for i in range(n+1):
    for j in range(i):
        prices[i] = max(prices[i], prices[j]+prices[i-j])
print(prices[-1])
