n = int(input())
time = list(map(int, input().split()))

time.sort()
total = 0
semi_total = 0
for t in time:
    semi_total += t
    total += semi_total
print(total)