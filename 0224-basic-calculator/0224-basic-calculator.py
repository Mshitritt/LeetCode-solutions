class Solution:
    def calculate(self, s: str) -> int:
        stuck = deque()
        res = 0
        num = 0
        neg = False
        for i in range(len(s)):
            curr = s[i]
            if curr != ')':
                if curr.isdigit():
                    if i+1 < len(s) and s[i+1].isdigit():
                        num *= 10
                        num += int(curr)
                    elif num:
                        num *= 10
                        num += int(curr)
                        if not neg:
                            stuck.append(num)
                        else:
                            stuck.append(-num)
                        num = 0
                    elif i == 0 or not neg:
                        stuck.append(int(curr))
                    else:
                        stuck.append(-int(curr))
                        neg = False
                if curr == '-':
                    neg = not neg
            else:
                while stuck:
                    res += stuck.pop()
                
                
            
        
        while stuck:
            res += stuck.pop()
        return res