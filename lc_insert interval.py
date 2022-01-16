def insert(intervals, newInterval):
    answer = []
    if intervals:
        maxi = max(intervals[-1][1], newInterval[1])
        intervalList = [[False, False] for _ in range(maxi+1)]
        for start, end in intervals:
            intervalList[start][0] = True # 머리임
            for i in range(start+1, end):
                intervalList[i][0] = True # 구간에 포함
            intervalList[end][1] = True #꼬리임
        # 새 구간 삽입
        if newInterval[0] == newInterval[1]:
            # 한구간이 점일 때,
            if intervalList[newInterval[0]] == [False, False]:
                # 그 구간에 값이 없었을 경우
                intervalList[newInterval[0]] = [True, True]
            else:
                pass
        else:
            intervalList[newInterval[0]][0] = True #머리
            intervalList[newInterval[0]][1] = False # 머리
            for i in range(newInterval[0]+1, newInterval[1]):
                intervalList[i][0] = True
                intervalList[i][1] = False
            # 꼬리가 구간이 아예 아니였을 경우
            if intervalList[newInterval[1]] == [False, False]:
                intervalList[newInterval[1]][1] = True # 꼬리로 만들어줌

        temp = []
        for ind, el in enumerate(intervalList):
            isHead, isTail = el
            if isHead and not temp:
                # 머리이면
                temp.append(ind)
            if isTail and temp:
                # 꼬리이면
                temp.append(ind)
                answer.append(temp.copy())
                temp = []
        return answer
    else:
        return [newInterval]



intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))