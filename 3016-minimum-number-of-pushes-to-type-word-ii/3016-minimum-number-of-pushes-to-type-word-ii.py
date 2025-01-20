class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = list(Counter(word).most_common())
        
        res = 0
        count = 8
        taps = 1
        
        for l, f in freq:
            if count ==  0:
                taps += 1
                count = 8
            res += (f * taps)
            count -= 1
            
        return res