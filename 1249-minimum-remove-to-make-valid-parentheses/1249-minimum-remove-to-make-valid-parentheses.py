class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        q = deque()
        for c in s:
            if c != '(' and c != ')':
                res.append(c)
            else:
                if c == '(':
                    q.append(c)
                    res.append(c)
                else:
                    # c = ')
                    if q:
                        temp = q.pop()
                        if temp == '(':
                            res.append(c)
        i = len(res)-1
        while q and i >= 0:
            if res[i] == '(':
                q.pop()
                res.pop(i)
        
            i -= 1
        
            
        return "".join(res)