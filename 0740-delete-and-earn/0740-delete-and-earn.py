class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        maxNum = max(nums)
        freq = Counter(nums)
        if len(freq) == 1:
            return nums[0]*freq[nums[0]]
        dp = [-1]*(maxNum+1)
        dp[0] = 0
        
        def rec(i):
            if i > maxNum:
                return 0
            while i not in freq and i <= maxNum:
                i += 1
            a = -1
            b = -1
            if i + 1 < maxNum and dp[i+1] != -1:
                a = dp[i+1]
            else:
                a = rec(i+1)
                if i+1 < maxNum:
                    dp[i+1] = a
            if i + 2 < maxNum and dp[i+2] != -1:
                b = dp[i+2]
                if i+2 < maxNum:
                    dp[i+2] = b
            else:
                b = rec(i+2)

            c = (freq[i] * i)
            return max(a, b+c)
        
        for i in range(1, maxNum):
            dp[i] = rec(i)
        return max(dp)

        """
        if not nums:
            return 0

        # Find the maximum value in nums to set up our dp array
        max_num = max(nums)

        # Create a frequency map to calculate total points for each number
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num

        # Use a dp array to solve the problem similar to the "House Robber Problem"
        dp = [0] * (max_num + 1)
        dp[0] = 0
        dp[1] = points[1]

        # Fill the dp array using the transition relation
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])

        # The answer is the maximum points we can earn
        return dp[max_num]
        """
                



        


