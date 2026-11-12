class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, z_cnt = 1, 0
        res = [0] * len(nums)
        for num in nums:
            if num != 0:
                prod *= num
            else:
                z_cnt += 1
        
        if z_cnt > 1:
            return res
        elif z_cnt == 1:
            idx = nums.index(0)
            res[idx] = prod
        else:
            for i, c in enumerate(nums):
                res[i] = prod // c
        return res
