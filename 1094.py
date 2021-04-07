x = int(input())
xBin = bin(x)[2:]
count = 0
for l in xBin:
    if l =='1':
        count +=1
print(count)