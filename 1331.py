path = []
positions = set()
row = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
for _ in range(36):
    move = input()
    positions.add(move)
    path.append([row[move[0]], int(move[1])])

def dist(a, b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

# 모든 점 방문했는지 확인
if len(list(positions)) != 36:
    print('Invalid')
else:
    # 끝 점에서 첫점 가능?
    last = path[-1]
    first = path[0]
    if dist(last, first) != 5:
        print('Invalid')
    else:
        for ind, el in enumerate(path[:-1]):
            if dist(el, path[ind+1]) != 5:
                print('Invalid')
                break
        else:
            print('Valid')
