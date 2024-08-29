class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = m - 1
        l2 = n - 1
        while l1 >= 0 or l2 >= 0:
            if l1 >= 0 and l2 >= 0:
                if nums1[l1] < nums2[l2]:
                    nums1.insert(l1+1, nums2[l2])
                    nums1.pop()
                    l2 -= 1
                else:
                    l1 -= 1
            elif l1 < 0 and l2 >= 0:
                nums1.insert(0, nums2[l2])
                nums1.pop()
                l2 -= 1
            else:
                l1 -= 1
            
                

                
