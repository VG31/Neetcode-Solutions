from collections import deque

class Solution:

    def bfs(self, x, y, visited, n, m, grid):

        q = deque()
        q.append((x,y))
        visited.add((x,y))

        while q:
            r,c = q.popleft()

            dc = [0, 1, 0, -1]
            dr = [1, 0, -1, 0]

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]=='1' and (nr,nc) not in visited:
                    q.append((nr,nc))
                    visited.add((nr,nc))


    def numIslands(self, grid: List[List[str]]) -> int:


        n = len(grid)
        m = len(grid[0])

        visited = set()

        cnt = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in visited:
                    self.bfs(i,j,visited, n, m, grid)
                    cnt += 1
        
        return cnt

