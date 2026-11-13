class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l += 1
            elif nums[m] < nums[r]:
                r -= 1
            else:
                break
        return nums[m]