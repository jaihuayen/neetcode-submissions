class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dirc = [[-1,0],[1,0],[0,1],[0,-1]]

        q = deque()
        fresh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1      
        if fresh == 0:
            return 0
        
        cnt = 0
        while (q and fresh > 0):
            for _ in range(len(q)):
                r, c = q.popleft()
                for d in dirc:
                    nr, nc = r + d[0], c + d[1]
                    if nr >= row or nr < 0 or nc >= col or nc < 0:
                        continue
                    if grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            cnt += 1
        return cnt if fresh == 0 else -1
