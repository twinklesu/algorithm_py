n = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

left = 0
right = n-1
smallest = 10**10
smallest_left = -1
smallest_right = -1

while left < right:
    new_value = abs(numbers[left]+numbers[right])
    if new_value <= smallest:
        smallest = new_value
        smallest_left = left
        smallest_right = right
    if abs(numbers[left]) > abs(numbers[right]):
        left += 1
    elif abs(numbers[left]) < abs(numbers[right]):
        right -= 1
    else:
        break

print(numbers[smallest_left], numbers[smallest_right])
