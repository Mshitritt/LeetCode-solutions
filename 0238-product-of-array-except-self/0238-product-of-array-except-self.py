class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        mul = 1
        # search a zero in nums
        zero_index = -1
        for i in range(n):
            if nums[i] != 0:
                mul *= nums[i]
            else:
                if zero_index != -1:
                    return ans
                else:
                    zero_index = i

        # exist only 1 zero in array
        if zero_index != -1:
            ans[zero_index] = mul
            return ans

        # calculate products
        for i in range(n):
            if i != zero_index:
                ans[i] = mul // nums[i]

        return ans
