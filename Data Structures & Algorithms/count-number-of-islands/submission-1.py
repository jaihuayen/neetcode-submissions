class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirc = [[-1,0], [0, -1], [1, 0], [0, 1]]
        island = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0":
                    continue
                island += 1
                grid[i][j] = "0"
                q = deque([(i, j)])
                while q:
                    r, c = q.popleft()
                    for k in dirc:
                        if r + k[0] >= rows or c + k[1] >= cols or r + k[0] < 0 or c + k[1] < 0:
                            continue
                        if grid[r + k[0]][c + k[1]] == "1":
                            q.append((r + k[0], c + k[1]))
                            grid[r + k[0]][c + k[1]] = "0"
        return island
                
                        