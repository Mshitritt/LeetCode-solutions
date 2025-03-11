class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        if n == 1:
            return 1
        curr_1, curr_2 = 1, 1
        
        res = 1

        for i in range(1, n):
            n1, n2 = nums1[i], nums2[i]
            temp_1, temp_2 = 1, 1

            # Ending nums1
            if n1 >= nums1[i-1]:
                temp_1 = curr_1 + 1
            if n1 >= nums2[i-1]:
                temp_1 = max(temp_1, curr_2 + 1)
            
            

            # Ending nums2
            if n2 >= nums2[i-1]:
                temp_2 = curr_2 + 1
            if n2 >= nums1[i-1]:
                temp_2 = max(temp_2, curr_1 + 1)

            # Update result
            curr_1, curr_2 = temp_1, temp_2
            res = max(res, curr_1, curr_2)
        
        return res
            
        



