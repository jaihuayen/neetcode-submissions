class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(m):
            if m >= n:
                return m == n
            if cache[m] != -1:
                return cache[m]
            cache[m] = dfs(m + 1) + dfs(m + 2)    
            return cache[m]
        return dfs(0)