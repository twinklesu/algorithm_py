def getVector(u, v):
    return [u[0]-v[0], u[1]-v[1]]


p1, p2, p3 = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))

p12 = getVector(p1, p2)
p13 = getVector(p1, p3)

# outer product
