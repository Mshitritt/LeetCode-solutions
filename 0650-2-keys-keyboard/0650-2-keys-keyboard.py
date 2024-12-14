class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        memo = {}
        def rec(k, lstA):
            if k > n:
                return float('inf')
            if k == n:
                return 1
            if (k, lstA) in memo:
                return memo[(k, lstA)]
            
            # copy+past
            op1 = 2 + rec(k+lstA, k+lstA)

            # past
            op2 = 1 + rec(k+lstA, lstA)
            memo[(k, lstA)] = min(op1, op2)
            return min(op1, op2)
        
        return rec(1, 1)
            
            
