
n,k = input().split()
n, k =int(n), int(k)
li = list(range(1, n+1))
result = "<"
pointer = 0
while len(li) !=1:
    for _ in range(k-1):
        if pointer ==len(li):
            pointer = 0
        pointer +=1
    if pointer == len(li):
        pointer = 0
    result += str(li.pop(pointer))
    result += ", "
result += str(li[0])
result += ">"
print(result)

