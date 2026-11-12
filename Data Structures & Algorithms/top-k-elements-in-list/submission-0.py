class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
        for num, cnt in dic.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res