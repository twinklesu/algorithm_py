n, m = map(int, input().split())
a = set()
b = set()
for _ in range(n):
    a.add(input())
for _ in range(m):
    b.add(input())

intersect = a.intersection(b)
print(len(intersect))
intersect = list(intersect)
intersect.sort()
for i in intersect:
    print(i)