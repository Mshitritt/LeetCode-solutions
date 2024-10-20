class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # -2, -1, 0, 0, 2 -- target = 0 
        nums.sort()
        res = []
        n = len(nums)

        for idx in range(n):
            if idx > 0 and nums[idx-1] == nums[idx]:
                continue
            r1 = nums[idx]

            # 3-sum problem
            for i in range(idx+1, n):
                if i > idx+1 and nums[i-1] == nums[i]:
                    continue
                r2 = nums[i]

                left = i + 1
                right = n - 1
                while left < right:
                    if r1 + r2 + nums[left] + nums[right] == target:
                        res.append([r1, r2, nums[left], nums[right]])
                        # Move both pointers and skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    else:
                        if r1 + r2 + nums[left] + nums[right] > target:
                            right -= 1
                        else:
                            left += 1
        return res

                         
                        

