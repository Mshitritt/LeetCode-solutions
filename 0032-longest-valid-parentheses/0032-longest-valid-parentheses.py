class Solution:
    def longestValidParentheses(self, s: str) -> int:
        q = deque()
        res = 0
        lstValid = -1
        
        for i, l in enumerate(s):
            if l == '(':
                q.append(i)
            else:
                if q:
                    q.pop()
                    if q:
                        res = max(res, i - q[-1])
                    else:
                        res = max(res, i-lstValid)
                else:
                    lstValid = i


                

            

        return res



