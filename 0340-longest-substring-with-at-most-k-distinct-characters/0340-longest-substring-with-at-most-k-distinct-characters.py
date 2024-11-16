class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        r = 0
        disitinct = {}
        res = 0
        if not k:
            return res
        while r < len(s):
            curr = s[r]
            if curr in disitinct:
                r += 1
            else:
                if k > 0:
                    k -= 1
                    disitinct[curr] = 1
                    r += 1
                else:
                    # can't add any new character 
                    res = max(res, r - l)
                    disitinct[s[l]] -= 1
                    if disitinct[s[l]] == 0:
                        del disitinct[s[l]]
                    l += 1
                    k += 1
        return max(res, r-l)



        

