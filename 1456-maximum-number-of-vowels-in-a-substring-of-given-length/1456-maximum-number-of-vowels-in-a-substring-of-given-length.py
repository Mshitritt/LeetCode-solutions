class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        countMax = 0
        for i in range(k):
            if s[i] in vowels:
                countMax += 1
        
        i = k
        count = countMax
        while i < len(s):
            if count == k:
                return k
            else:
                if s[i-k] in vowels:
                    count -= 1
                if s[i] in vowels:
                    count += 1
                i += 1
                countMax = max(countMax, count)
        return countMax



        
