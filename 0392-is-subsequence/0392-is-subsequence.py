class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s sub of t
        t_len = len(t)
        s_len = len(s)
        """
        2 null --> true
        s = null --> true
        t = null --> false 

        """
        if t_len ==0 and s_len ==0:
            return True 
        if t_len == 0:
            return False

        i_t = 0
        i_s = 0
        
        while i_t < t_len and i_s < s_len:
            if s[i_s] == t[i_t]:
                i_s += 1
            i_t += 1

        if i_s == s_len:
            return True
        else:
            return False
        