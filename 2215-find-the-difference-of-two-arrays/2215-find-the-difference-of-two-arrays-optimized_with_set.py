class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1)  # Convert nums1 to a set
        set_nums2 = set(nums2)  # Convert nums2 to a set

        # Find elements in nums1 not in nums2 and vice versa
        ans1 = list(set_nums1 - set_nums2)
        ans2 = list(set_nums2 - set_nums1)

        return [ans1, ans2]