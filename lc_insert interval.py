def insert(intervals, newInterval):
    answer = []
    if intervals:
        if newInterval[1] < intervals[0][0]:
            # 새 구간이 현재 구간 아래
            answer.append(newInterval)
            answer.extend(intervals)
            return answer
        if intervals[-1][1] < newInterval[0]:
            # 현재 모든 구간이 새 구간의 아래
            answer.extend(intervals)
            answer.append(newInterval)
            return answer
        # 새 구간이 현재 구간들 사이에 있으며 겹쳐질 수 있음
        insertInterval = newInterval.copy()
        for interval in intervals:
            intervalStart, intervalEnd = interval
            # break 조건
            if newInterval[1] < intervalStart:
                break
            if intervalStart <= newInterval[0] <= intervalEnd:
                insertInterval[0] = intervalStart
            if intervalStart <= newInterval[1] <= intervalEnd:
                insertInterval[1] = intervalEnd
        isInserted = False
        for start, end in intervals:
            if end < insertInterval[0]:
                answer.append([start, end])
            elif insertInterval[1] < start:
                if not isInserted:
                    answer.append(insertInterval)
                    isInserted = False
                answer.append([start, end])
        return answer
    else:
        return [newInterval]



intervals = [[3,5],[12,15]]

newInterval = [6,6]
print(insert(intervals, newInterval))