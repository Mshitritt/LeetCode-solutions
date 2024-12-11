class Solution:
    def minimumDeletions(self, s: str) -> int:
        

        a_count = 0
        b_count = 0
        for l in s:
            if l == 'a':
                a_count += 1
            else:
                b_count += 1
        
        
        
        res = min(a_count, b_count)
        
        a_curr = 0
        b_curr = 0
        

        for i in range(len(s)):
            if s[i] == 'a':
                a_curr += 1
            else:
                b_curr += 1
            
            a_right = a_count - a_curr
            #b_left = b_curr

            res = min(res, b_curr + a_right)
        return res


        


