class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = m - 1
        l2 = n - 1
        k = m + n - 1
        while l2 >= 0: # because we want to move element of nums2
            if l1 >= 0 and nums1[l1] > nums2[l2]:
                nums1[k] = nums1[l1]
                l1 -= 1
            else:
                nums1[k] = nums2[l2]
                l2 -= 1
            k -= 1
            
                

                
