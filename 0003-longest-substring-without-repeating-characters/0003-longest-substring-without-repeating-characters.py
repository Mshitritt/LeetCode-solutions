class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        freq = {}
        res = 1
        
        for r in range(len(s)):
            curr = s[r]
            if curr not in freq:
                freq[curr] = 1
                res = max(res, r-l+1)
            else:
                freq[curr] += 1
                while freq[curr] > 1:
                    freq[s[l]] -= 1
                    if not freq[s[l]]:
                        del freq[s[l]]
                    l += 1
        return res





