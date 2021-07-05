t = int(input())
for _ in range(t):
    n = int(input())
    permu = list(map(int, input().split()))
    permudict = dict()
    for ind, el in enumerate(permu):
        permudict[ind+1] = el

    count = 0
    for i in range(1, n+1):
        thisNode = permudict[i]
        if thisNode != 0:
            permudict[i] = 0
            while thisNode != 0:
                nextNode = permudict[thisNode]
                permudict[thisNode] = 0
                thisNode = nextNode
            count += 1
    print(count)
