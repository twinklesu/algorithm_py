import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
tree = list(map(int, input().rstrip().split()))

h = max(tree)
total = 0

li = [0 for _ in range(h)]
for t in tree:
    for n in range(t):
        li[n] += 1
li.append(0)
for l in li[::-1]:
    total += l
    if total >= m:
        break
    h -= 1
print(h)