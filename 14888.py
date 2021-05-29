from itertools import permutations

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a < 0:
        return -1 * (abs(a)//b)
    return a//b

n = int(input())
numbers = list(map(int, input().split()))
numOfOperator = list(map(int, input().split()))
operator = [add for _ in range(numOfOperator[0])] + [sub for _ in range(numOfOperator[1])] + [mul for _ in range(numOfOperator[2])] + [div for _ in range(numOfOperator[3])]
perm = set(permutations(operator))

calc_number = set()
for opp in perm:
    temp = numbers[0]
    for num, op in zip(numbers[1:],opp):
        temp = op(temp, num)
    calc_number.add(temp)

print(max(calc_number))
print(min(calc_number))