# global
mem = dict()
mem[0] = [1,0]
mem[1] = [0,1]


def fib(n):
    if n in mem:
        return mem[n]
    else:
        n_1 = fib(n-1)
        n_2 = fib(n-2)
        mem[n] = [n_1[0]+n_2[0], n_1[1]+n_2[1]]
        return mem[n]

def solution(n):
    ans = fib(n)
    print(ans[0], ans[1])


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        solution(n)


main()