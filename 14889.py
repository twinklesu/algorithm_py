from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    line = list(map(int, input().rstrip().split()))
    for ind, el in enumerate(line):
        matrix[i][ind] = el

num = list(range(n))
comb = list(combinations(num, n//2))
comb = comb[:len(comb)//2]

def diff(arr):
    return abs(arr[0]-arr[1])

li = []
for start in comb:
    temp = [0,0]
    link = list(set(num).difference(set(start)))
    for startI, linkI in zip(start, link):
        for startJ, linkJ in zip(start, link):
            temp[0] += matrix[startI][startJ]
            temp[1] += matrix[linkI][linkJ]
    li.append(diff(temp))

print(min(li))