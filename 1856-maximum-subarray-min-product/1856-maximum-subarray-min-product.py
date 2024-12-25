class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        q = deque() # store minimum index
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        res = 0

        for i, num in enumerate(nums):
            prefix[i] = (prefix[i-1] + nums[i]) if i > 0 else nums[0]
            while q and num < nums[q[-1]]:
                min_index = q.pop()
                min_value = nums[min_index]


                left_bound = q[-1] if q else -1
                total = prefix[i - 1] - (prefix[left_bound] if left_bound >= 0 else 0)
                
                minProduct = min_value  * total
                res = max(res, minProduct)

            q.append(i)
            

        # calculate min-product for the rest elements in q
        while q:
            min_index = q.pop()
            min_value = nums[min_index]
            left_bound = q[-1] if q else -1
            total = prefix[len(nums) - 1] - (prefix[left_bound] if left_bound >= 0 else 0)
            min_product = min_value * total
            res = max(res, min_product)

        return res % (10**9 + 7)


