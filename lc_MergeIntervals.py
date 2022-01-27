def merge(intervals):
    answer = []
    intervals.sort()
    semiAns = intervals[0]
    for start, end in intervals[1:]:
        if start <= semiAns[1]:
            # overlapped
            semiAns[1] = max(semiAns[1], end) # new interval's end can be bigger
        else:
            answer.append(semiAns.copy())
            semiAns = [start, end]
    answer.append(semiAns)
    return answer

merge([[2,3],[4,5],[6,7],[8,9],[1,10]])