class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        nums = [1, 7, 3, (6), 5, 6]
        l_sum= [0, 1, 8, 11, 17, 22]
        r_sum=[27, 20, 17, 11, 6, 0]
        """
        n = len(nums)
        l_sum = [0]*n
        r_sum = [0]*n

        for i in range(1, n):
            l_sum[i] = l_sum[i-1] + nums[i-1]

        for i in range(n-2, -1, -1):
            r_sum[i] = r_sum[i+1] + nums[i+1]

        for i in range(n):
            if l_sum[i] == r_sum[i]:
                return i
        
        return -1
