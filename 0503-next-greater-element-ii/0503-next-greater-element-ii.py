class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        newNums = []
        for num in nums:
            newNums.append(num)

        for num in nums:
            newNums.append(num)

        numsIdx = defaultdict(list)
        for idx, val in enumerate(newNums):
            numsIdx[val].append(idx % len(nums))

        res = [-1]*len(nums)
        stack = []
        for i in range(len(newNums)):
            curr = newNums[i]
            while stack and stack[-1] < curr:
                num = stack.pop(-1)
                idx = numsIdx[num].pop(0)
                if res[idx] == -1:
                    res[idx] = curr
            
            stack.append(curr)
        
        return res