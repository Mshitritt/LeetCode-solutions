class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {}
        for idx, val in enumerate(nums1):
            nums1Idx[val] = idx

        res = [-1]*len(nums1)
        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and stack[-1] < curr:
                num = stack.pop(-1)
                idx = nums1Idx[num]
                res[idx] = curr
            
            if curr in nums1Idx:
                stack.append(curr)
        return res

