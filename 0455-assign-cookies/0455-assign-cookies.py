class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # check how namy elements in s >= g elements 
        # s can be empty 
        """
        
        g.sort()
        s.sort()
        i_s = len(s)-1
        i_g = len(g)-1
        count = 0
        while i_s >= 0 and i_g >= 0:
            if s[i_s] >= g[i_g]:
                count += 1
                i_s -= 1
            
            i_g -= 1

        return count
        """
        g.sort(reverse=True)
        s.sort(reverse=True)
        i=0
        j=0
        c=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                c+=1
                j+=1
            i+=1
        return c

