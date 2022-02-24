from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowN = len(grid)
        colN = len(grid[0])

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        count = 0

        for i in range(rowN):
            for j in range(colN):
                if grid[i][j] == "1":
                    count += 1
                    q = deque()
                    grid[i][j] = "0"
                    q.append([i, j])
                    while q:
                        r, c = q.popleft()
                        for k in range(4):
                            x = r + dx[k]
                            y = c + dy[k]
                            if 0 <= x < rowN and 0 <= y < colN and grid[x][y] == "1":
                                q.append([x, y])
                                grid[x][y] = "0"
        return count