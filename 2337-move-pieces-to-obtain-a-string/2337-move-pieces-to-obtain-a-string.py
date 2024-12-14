class Solution:
    def canChange(self, start: str, target: str) -> bool:
        l_count_start = start.count('L')
        r_count_start = start.count('R')
        l_count_target = target.count('L')
        r_counter_target = target.count('R')
        # edge case 1
        if l_count_start != l_count_target or r_count_start != r_counter_target:
            return False
        
       
        
        si, ti = 0, 0
        n = len(start)
        while si < n and ti < n:
            # get first letter from start
            while si < n and start[si] == '_':
                si += 1
            
            # get first letter fron target
            while ti < n and target[ti] == '_':
                ti += 1

            # edge case if at least one of the strings over
            if si == ti == n:
                return True
            if si == n or ti == n:
                return False

            # check for iligal movement 
            if start[si] == 'R' and si > ti:
                return False
            if start[si] == 'L' and si < ti:
                return False
            if start[si] != target[ti]:
                return False
            
            # no more breaking rules
            si += 1
            ti += 1
        
        return True
        
        
                

            
            


        
        
            




            
