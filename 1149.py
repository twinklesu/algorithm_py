import sys
input = sys.stdin.readline


t = int(input())
price = []
for _ in range(t):
    price.append(list(map(int, input().split())))

acc_cost = [0,0,0]

for p in price:
    newRed = p[0] + min(acc_cost[1:])
    newGreen = p[1] + min(acc_cost[0], acc_cost[2])
    newBlue = p[2] + min(acc_cost[:2])
    acc_cost = [newRed, newGreen, newBlue]

print(min(acc_cost))
