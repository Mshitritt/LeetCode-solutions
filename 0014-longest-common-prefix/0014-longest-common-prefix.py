class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        minWord = float('inf')
        for s in strs:
            minWord = min(minWord, len(s))
        
        for i in range(minWord):
            l = strs[0][i]
            for s in strs:
                if s[i] != l:
                    return res
            res += l
        return res

