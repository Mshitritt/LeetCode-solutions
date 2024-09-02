class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [2, 3, 4, 5]
        ans = [60, 40, 30, 24]

        prod_l = [1, 2, 6, 24]  # contain multiple all left element
        prod_r = [60, 20, 5, 1]  # contain multiple all right element
        ans = prod_l[i] * prod_r[i]
        """
        n = len(nums)
        ans = [0]*n
        prod_l = [1]*n
        prod_r = [1]*n

        # fill prod_l
        for i in range(1, n):
            prod_l[i] = nums[i-1] * prod_l[i-1]

        # fill prod_r
        for i in range(n-2, -1, -1):
            prod_r[i] = nums[i+1] * prod_r[i+1]

        # calculate ans
        for i in range(n):
            ans[i] = prod_l[i] * prod_r[i]

        return ans
