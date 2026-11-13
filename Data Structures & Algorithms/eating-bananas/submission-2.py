class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l<=r:
            m = (l + r) // 2
            time = 0
            for p in piles:
                if p % m > 0:
                    time = time + p // m + 1
                else:
                    time += p // m
            if time <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
                
