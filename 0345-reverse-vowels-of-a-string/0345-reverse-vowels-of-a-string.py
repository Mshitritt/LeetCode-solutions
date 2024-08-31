class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowels(a):
            a = a.capitalize()
            if a == 'A' or a == 'E' or a == 'I' or a == 'O' or a == 'U':
                return True
            else:
                return False

        l = 0
        r = len(s)-1
        lst = list(s)

        while l < r:
            if isVowels(lst[l]) and isVowels(lst[r]):
                lst[l], lst[r] = lst[r], lst[l]
                r -= 1
                l += 1
            else:
                if isVowels(lst[l]):
                    r -= 1
                else:
                    l += 1
        
        return ''.join(lst)
