class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        bisect_left(nums, nums[i]-1, 0, i)
        """
 
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Create a new array to store result
        result = nums.copy()
        
        # Step 3: Place the smaller half and larger half 
        # alternately to create wiggle sort
        n = len(nums)
        mid = (n - 1) // 2
        large = n - 1
        
        # Fill even indices with smaller numbers
        # Fill odd indices with larger numbers
        for i in range(n):
            if i % 2 == 0:
                nums[i] = result[mid]
                mid -= 1
            else:
                nums[i] = result[large]
                large -= 1

        