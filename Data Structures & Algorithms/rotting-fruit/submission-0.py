from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        n = len(grid)
        m = len(grid[0])

        q = deque()

        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        time = 0 

        while q:
            r, c, t = q.popleft()

            time = max(time, t)

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr>=0 and nc>=0 and nr<n and nc<m and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, t + 1))

        
        if fresh > 0:
            return -1

        return  time



