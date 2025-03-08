class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[0] for nums 1
        # dp[1] for nums 2
        dp = [[1, 1] for _ in range(len(nums1))]    
        res = 1

        for i in range(1, len(nums1)):
            n1, n2 = nums1[i], nums2[i]

            # end with nums 1 
            if n1 >= nums1[i-1]:
                dp[i][0] = max(dp[i][0], dp[i-1][0]+1)
            if n1 >= nums2[i-1]:
                dp[i][0] = max(dp[i][0], dp[i-1][1]+1)

            # end with nums 2
            if n2 >= nums2[i-1]:
                dp[i][1] = max(dp[i][1], dp[i-1][1]+1)
            if n2 >= nums1[i-1]:
                dp[i][1] = max(dp[i][1], dp[i-1][0]+1)

            res = max(res, dp[i][0], dp[i][1])
        
        return res



