class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        def rec(i, M, aliceTurn):
            if i >= len(piles):
                return 0
            if (i, M, aliceTurn) in memo:  # Check memo
                return memo[(i, M, aliceTurn)]

            if aliceTurn:
                maxAlice = 0
                total = 0
                for j in range(i, min(len(piles), i + 2*M)):
                    total += piles[j]
                    maxAlice = max(maxAlice, total + rec(j + 1, max(M, j - i + 1), False))
                memo[(i, M, aliceTurn)] = maxAlice
                return maxAlice
            else:
                minAlice = float('inf')
                for j in range(i, min(len(piles), i + 2*M)):
                    minAlice = min(minAlice, rec(j + 1, max(M, j - i + 1), True))
                memo[(i, M, aliceTurn)] = minAlice
                return minAlice

                
            
        
        return rec(0, 1, True)
        
        
                




        