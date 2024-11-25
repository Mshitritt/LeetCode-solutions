class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        need = total // 2
        dp = [False]*(need+1)
        
        dp[0] = True
        for curr in nums:
            for j in range(need, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]
        return dp[need]

        """
        total = sum(nums)
        if total % 2 == 1:
            return False
        need = total // 2
        dp = [[False for _ in range(need+1)]for _ in range(len(nums)+1)]
        
        dp[0][0] = True
        for r in range(1, len(nums)+1):
            curr = nums[r-1]
            for c in range(need+1):
                
                if curr <= c: 
                    dp[r][c] = dp[r-1][c] or dp[r-1][c-curr]
                else: 
                    dp[r][c] = dp[r-1][c]
        for r in dp:
            print(r)
        return dp[len(nums)][need]
        """     
        
