def howManyIn(n, k):
    count = 0
    division = k
    while n >= division:
        count += n//division
        division *= k
    return count


n, m = map(int, input().split())
two = howManyIn(n, 2) - howManyIn(m,2) - howManyIn(n-m,2)
five = howManyIn(n, 5) - howManyIn(m,5) - howManyIn(n-m,5)
print(min(two, five))