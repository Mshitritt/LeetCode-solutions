class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = "", ""
        l_res, r_res = 0, 0
        minVal = float('inf')
        opIdx = None
        
        # find the operation
        for i, char in enumerate(expression):
            if char == "+":
                left = expression[:i]
                right = expression[i+1:]
                minVal = int(left) + int(right)
                opIdx = i

        # find the minimum result
        
        n = len(expression)
        for il in range(len(left)):
            for ir in range(len(right)):
                # il - how many digits remove from start's left
                # ir - how many digits remove from end's right
                leftNum = int(expression[il:opIdx])
                leftRest = int(expression[:il]) if expression[:il] else 1
                rightNum = int(expression[opIdx+1: n-ir])
                rightRest = int(expression[n-ir:]) if expression[n-ir:] else 1 
                # leftRest, leftNum, " + ", rightNum, rightRest
                val = leftRest * (leftNum + rightNum) * rightRest
                if val < minVal:
                    minVal = val
                    l_res, r_res = il, ir
        

        
        # buils the result expression 
        final = expression[:l_res] + '(' + expression[l_res:n-r_res] + ')' + expression[n-r_res:]
        return final


        