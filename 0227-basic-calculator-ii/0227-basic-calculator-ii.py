class Solution:
    def calculate(self, s: str) -> int:
        res = 0

        i = 0
        stack = deque()
        curr = 0
        op = '+'
        for l in s:
            if l.isdigit():
                curr *= 10
                curr += int(l)
            elif l == " ":
                continue
            else:
                # l is operation
                if l in "+-" and op not in "*/":
                    if op == '-':
                        stack.append(-curr)
                    else:
                        stack.append(curr)
                    curr = 0
                    op = l
                else:
                    if op in "+-":
                        if op == '-':
                            stack.append(-curr)
                        else:
                            stack.append(curr)
                        curr = 0
                        op = l
                    else:
                        prev = stack.pop()
                        nxt = prev*curr if op == "*" else prev//curr
                        stack.append(nxt)
                        op = l
                        curr = 0
                    

        res = 0
        if curr:
            if op in "+-":
                res = curr if op == "+" else -curr
            elif op == '*':
                prev = stack.pop()
                stack.append(curr * prev)
            else:
                prev = stack.pop()
                if prev < 0:
                    prev *= -1 
                    nxt = prev // curr
                    nxt *= -1
                    stack.append(nxt)
                else:
                    stack.append(prev // curr)

        while stack:
            res += stack.pop()
        
        return res

            
            
            

            

            
            


