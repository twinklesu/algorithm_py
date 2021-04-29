from collections import deque

def solution():
    w, n = map(int, input().split())
    dest = []
    for _ in range(n):
        dest.append(list(map(int, input().split()))) # 거리, 용량
    dest = deque(dest)
    thisTurnWeight = 0
    totalDist = 0
    preDist = 0
    while dest:
        temp = dest.popleft()
        fromStart, weight = map(int, temp)
        fromPre = fromStart - preDist
        # 용량이 넉넉할 때
        if thisTurnWeight + weight < w:
            thisTurnWeight += weight
            totalDist += fromPre
            preDist = fromStart
            if not dest: # 마지막 지점
                totalDist += fromStart
        # 용량 딱 맞을 때
        elif thisTurnWeight + weight == w:
            totalDist += fromPre
            if not dest: # 마지막 지점일 경우 편도.
                totalDist += fromStart
            else:
                totalDist += fromStart*2 # 비우고 다시 오기
                thisTurnWeight = 0
                preDist = fromStart
        else:
            totalDist += fromStart*2
            thisTurnWeight = 0
            dest.appendleft(temp)
    print(totalDist)



def main():
    n = int(input())
    for _ in range(n):
        solution()

main()