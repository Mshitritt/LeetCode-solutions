class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # Precompute suffix sums for quick total calculation
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        # Memoization dictionary
        memo = {}
        
        def rec(i, M, aliceTurn):
            # Base case: no more piles
            if i >= n:
                return 0
            
            # Check memoized result
            key = (i, M, aliceTurn)
            if key in memo:
                return memo[key]
            
            if aliceTurn:
                # Alice wants to maximize her score
                maxAlice = 0
                for j in range(i, min(n, i + 2*M)):
                    take = suffix_sum[i] - suffix_sum[j + 1]
                    maxAlice = max(maxAlice, take + rec(j + 1, max(M, j - i + 1), False))
                                
                
                memo[key] = maxAlice
                return maxAlice
            else:
                # Bob wants to minimize Alice's score
                minAlice = float('inf')
                for j in range(i, min(n, i + 2*M)):
                    minAlice = min(minAlice, 
                                rec(j + 1, max(M, j - i + 1), True))
                
                memo[key] = minAlice
                return minAlice
        
        return rec(0, 1, True)
        
                




        