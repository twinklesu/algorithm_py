n = int(input())
numbers = list(map(int, input().split()))

ind = n
for i in range(n-2, -1, -1):
    if numbers[i] < numbers[i+1]:
        ind = i
        break


if ind == n:
    print(-1)
else:
    change_target = 10  # 뒤부터 ind까지 중 큰 수
    for i in range(n-1, ind, -1):
        if numbers[ind] < numbers[i]:
            change_target = i
            break
    numbers[ind], numbers[change_target] = numbers[change_target], numbers[ind]
    numbers[ind+1:] = list(sorted(numbers[ind+1:]))
    print(*numbers)

