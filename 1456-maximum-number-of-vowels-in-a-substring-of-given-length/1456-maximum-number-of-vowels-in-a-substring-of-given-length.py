class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowels(l):
            if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
                return True
            return False

        countMax = 0
        for i in range(k):
            if isVowels(s[i]):
                countMax += 1
        
        i = k
        count = countMax
        while i < len(s):
            if count == k:
                return k
            else:
                if isVowels(s[i-k]):
                    count -= 1
                if isVowels(s[i+k-1]):
                    count += 1
                i += 1
                countMax = max(countMax, count)
        return countMax



        
