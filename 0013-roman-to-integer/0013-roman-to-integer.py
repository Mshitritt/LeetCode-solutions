class Solution:
    def romanToInt(self, s: str) -> int:
        symbole = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
        
        i = len(s)-1
        if i == 0:
            return symbole[s[0]]
        
        plus = 0
        minus = 0
        if symbole[s[0]] < symbole[s[1]]:
            minus += symbole[s[0]]
        else:
            plus += symbole[s[0]]
        while i >= 1:
            if symbole[s[i]] <= symbole[s[i-1]]:
                plus += symbole[s[i]]
                i -= 1
            else:
                plus += symbole[s[i]]
                minus += symbole[s[i-1]]
                i -= 2
            
        return plus - minus


        
