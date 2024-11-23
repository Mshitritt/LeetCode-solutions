class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        si = 0
        ei = 0
        l = 0
        r = 0
        freq_t = Counter(t)       
        win = defaultdict(int)
        need = len(freq_t)
        have = 0
        res = float('inf')

        currL = s[l]
        currR = s[r]
        
        while r < len(s):
            currL = s[l]
            currR = s[r]
            
            if s[r] in freq_t:
                win[s[r]] += 1
                if win[s[r]] == freq_t[s[r]]:
                    have += 1
            
            while have == need:
                # update results 
                if (r-l+1) < res:
                    si = l
                    ei = r
                    res = r-l+1

                # shrink
                if s[l] in win:
                    win[s[l]] -= 1
                    if win[s[l]] < freq_t[s[l]]:
                        have -= 1
                l += 1

            r += 1
  
        if res != float('inf'):
            return s[si: ei+1]
        return ""

            


            
        

                    
            
            


            
            

