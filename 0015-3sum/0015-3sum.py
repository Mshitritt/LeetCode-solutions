class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for idx in range(n):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            temp = []
            left = idx + 1
            right = n - 1
            while left < right:
                # -4, -1, -1, 0, 1, 2
                if nums[left] + nums[right] == -nums[idx]:
                    temp.append(nums[left])
                    temp.append(nums[right])
                    temp.append(nums[idx])
                    res.append(temp)

                    # Move both pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                    temp = []
                elif nums[left] + nums[right] > -nums[idx]:
                    right -= 1
                else:
                    left += 1
        return res


