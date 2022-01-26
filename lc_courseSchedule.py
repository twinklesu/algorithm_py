from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        status = [0 for _ in range(numCourses)]
        preToPost = defaultdict(list)
        for post, pre in prerequisites:
            status[post] += 1
            preToPost[pre].append(post)

        q = deque()
        countCourses = 0
        for num, state in enumerate(status):
            if state == 0:
                q.append(num)
                countCourses += 1
        while q:
            thisNode = q.popleft()
            for nextNode in preToPost[thisNode]:
                status[nextNode] -= 1
                if status[nextNode] == 0:
                    q.append(nextNode)
                    countCourses += 1
        if countCourses == numCourses:
            return True
        else:
            return False