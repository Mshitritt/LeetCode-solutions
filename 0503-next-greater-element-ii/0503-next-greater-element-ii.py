class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        numsIdx = defaultdict(list)
        for idx, val in enumerate(nums):
            numsIdx[val].append(idx)

        res = [-1]*len(nums)
        stack = []
        for i in range(len(nums)):
            curr = nums[i]
            while stack and stack[-1] < curr:
                num = stack.pop(-1)
                idx = numsIdx[num].pop(0)
                res[idx] = curr
            
            stack.append(curr)

        
        for i in range(len(nums)):
            if res[i] == -1 and stack and stack[0] > nums[i]:
                res[i] = stack.pop(0)
                
                
        
        
        return res