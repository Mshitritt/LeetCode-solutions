class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        freq = Counter(s)
        
        maxL, maxVal = s[0], 1
        for l, val in freq.items():
            if val > maxVal:
                maxVal = val
                maxL = l
        if maxVal > (len(s) + 1) // 2:
            return ""
        
        res = [""]*len(s)
        i = 0 

        # place the most common character 
        while freq[maxL]:
            res[i] = maxL
            freq[maxL] -= 1
            i += 2
        

        # place other characters 
        for l, val in freq.items():
            while val:
                if i >= len(s):
                    i = 1
                res[i] = l
                i += 2
                val -= 1

        
        return "".join(res)








