n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

ans = []
for a_, b_ in zip(a,b):
    ans.append(a_*b_)

print(sum(ans))