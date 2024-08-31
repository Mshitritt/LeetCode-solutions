class Solution:
    def reverseWords(self, s: str) -> str:
        lst = list(filter(lambda x: x != '', s.split(' ')))
        l = 0
        r = len(lst) - 1
        for i in range(1, r+1):
            lst[i] += ' '
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
        
        return ''.join(lst)
        