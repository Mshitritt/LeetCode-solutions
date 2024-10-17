class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for idx in range(n):
            temp = []
            left = idx + 1
            right = n - 1
            while left < right:
                # -4, -1, -1, 0, 1, 2
                if nums[left] + nums[right] == -nums[idx]:
                    temp.append(nums[left])
                    temp.append(nums[right])
                    temp.append(nums[idx])
                    #res.append(temp)
                    res.add(tuple(temp))
                    break
                elif nums[left] + nums[right] > -nums[idx]:
                    right -= 1
                else:
                    left += 1
        return list(res)


