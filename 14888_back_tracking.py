global max_, min_
max_ = -10**9-1
min_ = 10**9+1
def dfs(op, n, k, res, numbers):
    global max_, min_
    if k == n:
        if res < min_:
            min_ = res
        if res > max_:
            max_ = res
        return
    for i in range(4):
        # 더 이상 그 연산자를 사용할 수 없다면
        temp = res # 연산자 4개에 대한 계산 다 dfs로 넘겨야해서 이전의 결과 복사해서 쓰기
        if op[i] == 0:
            continue # 백트래킹 됨,,
        if i == 0:
            temp += numbers[k]
        elif i == 1:
            temp -= numbers[k]
        elif i == 2:
            temp *= numbers[k]
        elif temp < 0:
            temp = -1 * (abs(temp)//numbers[k])
        else:
            temp = temp//numbers[k]
        # 반복문 안에서 함수 호출해야 dfs
        op[i] -= 1
        dfs(op, n, k+1, temp, numbers)
        op[i] += 1

n = int(input())
numbers = list(map(int, input().split()))
numOfOperator = list(map(int, input().split()))
dfs(numOfOperator, n, 1, numbers[0], numbers)
print(max_)
print(min_)
