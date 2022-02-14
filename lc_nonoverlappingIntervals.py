from collections import deque

def eraseOverlapIntervals(intervals) -> int:
    intervals.sort()
    intervals = deque(intervals)
    count = 0

    while intervals:
        pre = intervals.popleft()
        if intervals:
            post = intervals.popleft()
        else:
            break

        if pre[1] > post[0]:
            # overlapped
            # 더 뒤에까지 영향을 주는 interval 제거
            if pre[1] < post[1]:
                # post를 제거
                intervals.appendleft(pre)
                count += 1
            else:
                # pre를 제거
                intervals.appendleft(post)
                count += 1
        else:
            # 겹쳐지지 않음. post는 뒤의 구간과 비교 위해서 다시 추가
            intervals.appendleft(post)
    return count


intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))