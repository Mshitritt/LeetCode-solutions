class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dict_nums1 = dict(Counter(nums1))
        dict_nums2 = dict(Counter(nums2))

        ans = [[], []]
        for num in nums1:
            if (num not in dict_nums2) and (num not in ans[0]):
                ans[0].append(num)

        for num in nums2:
            if (num not in dict_nums1) and (num not in ans[1]):
                ans[1].append(num)

        return ans