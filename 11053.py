n = int(input())
numbers = list(map(int, input().split()))

def solution(n,arr):
    result = [0 for _ in range(n+1)]
    maxlen = 0

    for n in arr:
        for j in range(maxlen,-1,-1):
            if result[j] < n:
                if j == maxlen:
                    maxlen = maxlen + 1
                    result[maxlen] = n
                else:
                    result[j+1] = min(result[j+1],n)
                break




    return maxlen



def main():
    n = int(input())
    arr = list(map(int,input().split()))
    print(solution(n,arr))

main()