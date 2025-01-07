class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        
        def isPalindrome(si, ei):
            while si < ei:
                if s[si] == s[ei]:
                    si += 1
                    ei -= 1
                else:
                    return False
            return True 
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    part.append(s[i: j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
        
        
                    


