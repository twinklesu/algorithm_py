from heapq import heappop, heappush

n, m = map(int, input().split())
card = list(map(int, input().split()))
heapCard = []
for c in card:
    heappush(heapCard, c)

for _ in range(m):
    one = heappop(heapCard)
    two = heappop(heapCard)
    heappush(heapCard, one+two)
    heappush(heapCard, one+two)


print(sum(heapCard))