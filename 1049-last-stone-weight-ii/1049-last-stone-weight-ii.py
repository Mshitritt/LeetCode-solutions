class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = ceil(stoneSum / 2)

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            if (i, total) in dp:
                print(f'{(i, total)}')
                return dp[(i, total)]

            withNum = dfs(i +1, total + stones[i])
            withoutNum = dfs(i+1, total)
            dp[(i, total)]=min(withNum, withoutNum)
            
            return dp[(i, total)]

        dp = {}
        
        ans = dfs(0, 0)
        """
        for key in dp:
            print(f'{key} - {dp[key]}')
            """
        return ans