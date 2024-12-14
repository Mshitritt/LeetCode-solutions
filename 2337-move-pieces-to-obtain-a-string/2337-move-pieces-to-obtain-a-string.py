class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        # edge case 1
        if start.count('L') != target.count('L') or start.count('R') != target.count('R'):
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
        
        
                

            
            


        
        
            




            
