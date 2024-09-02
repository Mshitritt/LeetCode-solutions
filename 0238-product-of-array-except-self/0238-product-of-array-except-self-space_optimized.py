class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [2, 3, 4, 5]
        ans = [60, 40, 30, 24]

        prod_l = [1, 2, 6, 24]  # contain multiple all left element
        prod_r = [60, 20, 5, 1]  # contain multiple all right element
        ans = prod_l[i] * prod_r[i]
        --------------------------------sol space O(1)
        same logic but in second loop calculate the right prod and ans prod
        """
        n = len(nums)
        ans = [1] * n  # Initialize the answer array with 1s

        # Fill the answer array with left products
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        # Right product initialization
        right_product = 1

        # Calculate right products and multiply with left products in the answer array
        for i in range(n - 1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]

        return ans
