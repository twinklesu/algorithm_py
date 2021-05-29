import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

# 합이 m 보다 작을 경우 end 포인터 증가
# 합이 m 보다 클 경우, start 포인터 증가
start = 0
end = 1
summed = 0
count = 0
while start < n and end < n+1:
    summed = sum(numbers[start:end])
    if summed == m:
        count += 1
        start += 1
    elif summed > m:
        start += 1
    else:
        end += 1

print(count)