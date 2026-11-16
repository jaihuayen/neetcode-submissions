class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        dirc = [[-1,0],[1,0],[0,1],[0,-1]]
        INF = 2147483647
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            r, c = q.popleft()
            for d in dirc:
                rd, cd = r + d[0], c + d[1]

                if rd >= row or rd < 0 or cd >=col or cd < 0 or grid[rd][cd] != INF:
                    continue
                
                grid[rd][cd] = grid[r][c] + 1
                q.append((rd,cd))