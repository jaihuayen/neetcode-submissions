class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list)
        for s in strs:
            store = [0] * 26
            for i in s:
                store[ord(i) - ord('a')] += 1
            hashset[tuple(store)].append(s)
        return list(hashset.values())