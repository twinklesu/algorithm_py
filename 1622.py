from collections import deque
while(True):
    a = list(map(str, input()))
    b = list(map(str, input()))

    if not a and not b:
        break

    a.sort()
    b.sort()
    aDeq = deque(a)
    bDeq = deque(b)

    answer = ''
    while aDeq and bDeq:
        aLetter = aDeq.popleft()
        bLetter = bDeq.popleft()
        if aLetter == bLetter:
            answer += aLetter
        elif aLetter < bLetter:
            bDeq.appendleft(bLetter)
        else:
            aDeq.appendleft(aLetter)
    print(answer)