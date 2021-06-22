import sys

input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
    times.append(list(map(int, input().rstrip().split())))

times.sort(key=lambda time : (time[1], time[0]))

endBefore = times[0][1]
count = 1
for time in times[1:]:
    if time[0] >= endBefore:
        count += 1
        endBefore = time[1]

print(count)
