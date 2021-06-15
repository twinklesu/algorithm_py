n = int(input())
numbers = list(map(int, input().split()))

# 처음으로 커지는 좌표 찾기
target_index = n
for i in range(n-2, -1, -1):
    if numbers[i] > numbers[i+1]:
        target_index = i
        break

if target_index == n:
    print(-1)
else:
    # 바꿀 수 찾기
    toChangeIndex = target_index +1
    for i in range(target_index+1, n):
        if numbers[target_index] > numbers[i] > numbers[toChangeIndex]:
            toChangeIndex = i
    numbers[target_index], numbers[toChangeIndex] = numbers[toChangeIndex], numbers[target_index]
    numbers[target_index+1:] = sorted(numbers[target_index+1:], reverse=True)

    print(*numbers)
