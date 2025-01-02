class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def rec(s):
            res = []
            if s in memo:
                return memo[s]

            if s.isdigit():
                return [int(s)]

            for i, char in enumerate(s):
                if char in "*+-":
                    # split into left and right 
                    left = rec(s[:i])
                    right = rec(s[i+1:])

                    # calculate results
                    for l in left:
                        for r in right:
                            if char == "+":
                                res.append(l + r)
                            elif char == "-":
                                res.append(l - r)
                            elif char == "*":
                                res.append(l * r)
                
            memo[s] = res
            return res

        return rec(expression)


            
