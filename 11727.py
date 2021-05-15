n = int(input())

dic = {1:1, 2:3}

for i in range(3, n+1):
    dic[i] = dic[i-2]*2 + dic[i-1]

print(dic[n]%10007)