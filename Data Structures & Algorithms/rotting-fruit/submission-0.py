from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        
        if fresh == 0:
            return 0
        
        mins = 0

        while q and fresh > 0:
            level = len(q)
            for _ in range(level):
                r_cur, c_cur = q.popleft()
                
                for dr, dc in dirs:
                    nr, nc = r_cur + dr, c_cur + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            mins += 1
        
        return mins if fresh == 0 else -1


        






                

