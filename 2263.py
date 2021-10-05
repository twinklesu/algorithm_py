import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

positionList = [0 for _ in range(n+1)] # 키가 inorder의 value, 이고, 값이 inorder의 index인
for ind, el in enumerate(inOrder):
    positionList[el] = ind

def recursion(inStart, inEnd, postStart, postEnd):
    if inStart==inEnd or postStart==postEnd:
        return
    root = postOrder[postEnd-1]
    print(root, end=' ')
    rootInd = positionList[root]
    recursion(inStart, rootInd, postStart, postStart+(rootInd-inStart))
    recursion(rootInd+1, inEnd, postStart+(rootInd-inStart), postEnd-1)


recursion(0, n, 0, n)