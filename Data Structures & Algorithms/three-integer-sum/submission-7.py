class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(1, len(nums) - 1):
            j, k = 0, len(nums) - 1
            while j <= k and j != i and k != i:
                if nums[i] > -(nums[j] + nums[k]):
                    k -= 1
                elif nums[i] < -(nums[j] + nums[k]):
                    j += 1
                else:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
        return res
