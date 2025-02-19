class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        
        freq = defaultdict(list)
        for s in strs:
            key = 0
            for l in s:
                key += ord(l) - ord('a')
            freq[key].append(s)
        
        res = []
        for _, s_list in freq.items():
            res.append(s_list)
        return res
