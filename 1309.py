n = int(input())
noLion = 1
left = 1
right = 1
for _ in range(n-1):
    newNo = (noLion + left + right)%9901
    newLeft = (noLion + right)%9901
    newRight = (noLion + left)%9901
    noLion, left, right = newNo, newLeft, newRight
print((noLion+left+right)%9901)