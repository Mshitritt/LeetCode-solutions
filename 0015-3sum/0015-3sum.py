class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        nums.sort()
        result = []
        
        # Step 2: Iterate over the array with the first pointer
        for i in range(len(nums) - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 3: Use two pointers
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # We found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    # If the sum is too small, move the left pointer to the right
                    left += 1
                else:
                    # If the sum is too large, move the right pointer to the left
                    right -= 1
        
        return result


