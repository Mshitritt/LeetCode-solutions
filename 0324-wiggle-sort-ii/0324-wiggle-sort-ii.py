class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        bisect_left(nums, nums[i]-1, 0, i)
        """
 
        def quickselect(k):
            """ QuickSelect algorithm to find the k-th smallest element in O(n) average time """
            def partition(left, right, pivot_index):
                pivot = nums[pivot_index]
                nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  # Move pivot to end
                store_index = left
                for i in range(left, right):
                    if nums[i] < pivot:
                        nums[store_index], nums[i] = nums[i], nums[store_index]
                        store_index += 1
                nums[right], nums[store_index] = nums[store_index], nums[right]  # Move pivot to its final place
                return store_index

            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_index = randint(left, right)
                new_pivot_index = partition(left, right, pivot_index)
                if new_pivot_index == k:
                    return nums[k]
                elif new_pivot_index < k:
                    left = new_pivot_index + 1
                else:
                    right = new_pivot_index - 1

        def virtual_index(i):
            """ Map index to the new index in the wiggle pattern """
            return (1 + 2 * i) % (len(nums) | 1)

        n = len(nums)
        
        # Step 1: Find median using QuickSelect
        median = quickselect(n // 2)

        # Step 2: Three-way partitioning (Dutch National Flag)
        left, i, right = 0, 0, n - 1
        while i <= right:
            vi = virtual_index(i)
            if nums[vi] > median:  # Place larger elements in odd indices
                nums[virtual_index(left)], nums[vi] = nums[vi], nums[virtual_index(left)]
                left += 1
                i += 1
            elif nums[vi] < median:  # Place smaller elements in even indices
                nums[virtual_index(right)], nums[vi] = nums[vi], nums[virtual_index(right)]
                right -= 1
            else:
                i += 1

        