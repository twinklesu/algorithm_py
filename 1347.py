n = int(input())
move = list(map(str, input().split('F')))
move = move[:-1]


arrow = 'S'
now = (0,0)
went = set()
went.add(now)
row = set()
col = set()
row.add(0)
col.add(0)
for m in move:
    if m == 'R' or m == 'LLL':
        arrow = 'W'
    elif m == 'RR' or m == 'LL':
        arrow = 'N'
    elif m == 'RRR' or m == 'L':
        arrow = 'E'
    if arrow == 'N':
        now = (now[0], now[1]+1)
    elif arrow == 'E':
        now = (now[0]-1, now[1])
    elif arrow == 'W':
        now = (now[0]+1, now[1])
    else:
        now = (now[0], now[1]-1)
    went.add(now)
    row.add(now[0])
    col.add(now[1])

rowN = len(row)
colN = len(col)
map_ = []
for r in range(rowN):
    temp = []
    for c in range(colN):
        temp.append('#')
    map_.append(temp)

rowMin = -min(row)
colMin = -min(col)
for w in went:
    x = w[0]+rowMin
    y = w[1]+colMin
    map_[x][y] = '.'
    print(x,y)
    print(map_)

for m in map_:
    for p in m:
        print(p, end='')
    print()

