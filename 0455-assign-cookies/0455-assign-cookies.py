class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # check how namy elements in s >= g elements 
        # s can be empty 
        """
        g = [1, 2, 3]
        s = [1, 1]
            --> 1
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
