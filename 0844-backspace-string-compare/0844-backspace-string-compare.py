class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ls = []
        lt = []
        i_s = 0
        i_t = 0
        while i_s < len(s):
            if s[i_s] == '#':
                if ls:
                    ls.pop()
            else:
                ls.append(s[i_s])
            i_s += 1
        
        while i_t < len(t):
            if t[i_t] == '#':
                if lt:
                    lt.pop()
            else:
                lt.append(t[i_t])
            i_t += 1
        
        return ls == lt


    