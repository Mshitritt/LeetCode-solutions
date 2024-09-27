class Solution:
    def isValid(self, s: str) -> bool:
        stuck = [] 
        i = 0
        while i < len(s):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stuck.append(s[i])
            else:
                if len(stuck) == 0:
                    return False
                # stuck not empty
                openBrace = stuck.pop()
                if openBrace == '(' and s[i] == ')':
                    pass
                elif openBrace == '{' and s[i] == '}':
                    pass
                elif openBrace == '[' and s[i] == ']':
                    pass
                else:
                    return False
            i += 1
        return True


            
        
