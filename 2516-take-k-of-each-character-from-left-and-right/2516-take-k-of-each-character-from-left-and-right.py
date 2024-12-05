class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        freq = Counter(s)
        chars = ['a', 'b', 'c']
        
        for c in chars:
            if c not in freq or freq[c] < k:
                return -1
            freq[c] -= k

        l = 0
        
        # expend - if left more than k elements of each charecter
        # shrink - else
        # find the largest valid window that left at least k elements of each charcter
        res = 0
        for r in range(len(s)):
            char_r = s[r]
            freq[char_r] -= 1

            while l <= r and freq[char_r] < 0:
                char_l = s[l]
                freq[char_l] += 1
                l += 1
            
            res = max(res, r-l+1)
        
     
                

        
        return len(s)-res
