class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        right = Counter(nums)
        if 1 not in nums:
            return [len(nums)]
        if 0 not in nums:
            return [0]
        
        left = {}
        left[0], left[1] = 0, 0
        zeros = 0
        
        highScore, score = right[0], 0
        # get the high score 
        for i in range(len(nums)):
            
            highScore = max(highScore, left[0] + right[1])
            
            if nums[i] == 0:
                zeros += 1

            left[nums[i]] += 1
            right[nums[i]] -= 1
        
        res = []
        # find all the highScores 
        right[0], right[1] = left[0], left[1]
        left[0], left[1] = 0, 0
        zeros = 0
        if right[0] == highScore:
            res.append(len(nums))
        for i in range(len(nums)):
            score = left[0] + right[1]
            if score == highScore:
                res.append(i)
            left[nums[i]] += 1
            right[nums[i]] -= 1
        return res
