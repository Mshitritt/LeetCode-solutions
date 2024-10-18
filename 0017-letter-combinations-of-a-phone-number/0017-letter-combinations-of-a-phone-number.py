class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digit_mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        comb = []
        def helper(temp, idx):
            if idx >= len(digits):
                comb.append(temp)
            else:
                for c in digit_mapping[digits[idx]]:
                    helper(temp + c, idx+1)
        
        helper("", 0)
        return comb
            
            

