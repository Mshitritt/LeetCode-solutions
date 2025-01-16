class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        bisect_left(nums, nums[i]-1, 0, i)
        """
 
        nums.sort()  # Step 1: Sort the array
        n = len(nums)

        # Step 2: Split into two halves and reverse both halves
        mid = (n + 1) // 2  # First half length
        smaller_half = nums[:mid][::-1]  # Reverse first half
        larger_half = nums[mid:][::-1]  # Reverse second half

        # Step 3: Interleave both halves
        i = 0
        for s, l in zip(smaller_half, larger_half):
            nums[i] = s  # Place in even index
            nums[i + 1] = l  # Place in odd index
            i += 2

        # Step 4: Handle the last remaining element for odd-length arrays
        if n % 2 == 1:
            nums[-1] = smaller_half[-1]
                

        