class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # freq = {} # Keep count of all frequencies
        # for n in nums:
        #     if n not in freq:
        #         freq[n] = 1
        #     else:
        #         freq[n] += 1
        freq = Counter(nums)

        # Remove duplicates and sort the array
        nums = list(set(nums))
        nums.sort()
        
        # Store the result of dp[i-1], and dp[i-2]
        prevprev, prev = 0, nums[0] * freq[nums[0]]
        # Go through all the numbers
        for i in range(1, len(nums)):
            # Get earnings of deleting this number
            curr = nums[i] * freq[nums[i]]
            # If we can just delete this without problem just add earnings
            if nums[i] > nums[i-1] + 1:
                curr += prev
            else: # Choice between deleting this + dp[i-2] or not deleting and just dp[i-1]
                curr += prevprev
                curr = max(curr, prev)
            
            # Update dp
            prevprev = prev
            prev = curr
        
        # Return last dp value
        return prev
        """
        maxNum = max(nums)
        freq = Counter(nums)
        if len(freq) == 1:
            return nums[0]*freq[nums[0]]
        dp = [-1]*(maxNum+1)
        dp[0] = 0
        self.res = 0
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
            if i + 2 < maxNum and dp[i+2] != -1:
                b = dp[i+2]
            else:
                b = rec(i+2)

            c = (freq[i] * i)
            dp[i] = max(a, b+c)
            self.res = max(self.res, dp[i])
            return dp[i]
        
        for i in range(1, maxNum):
            dp[i] = rec(i)
        return self.res
        """
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
                



        


