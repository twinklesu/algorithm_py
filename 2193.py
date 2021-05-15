n = int(input())
if n < 3:
    print(1) # 1과 2는 각각 1 과 10 뿐
else:
    n -= 2
    li = [[1,1]] # [0개수, 1개수]
    for i in range(1, n):
        temp = li[i-1]
        li.append([sum(temp), temp[0]])

    print(sum(li[-1]))