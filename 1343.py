board = input()
boardLi = map(str, board.split('.'))

ans = ''
for boardSet in boardLi:
    while len(boardSet) >=2:
        if len(boardSet) >= 4:
            boardSet = boardSet[4:]
            ans += 'AAAA'
        else:
            boardSet = boardSet[2:]
            ans += 'BB'
    if boardSet:
        print(-1)
        break
    ans += '.'
else:
    print(ans[:-1])