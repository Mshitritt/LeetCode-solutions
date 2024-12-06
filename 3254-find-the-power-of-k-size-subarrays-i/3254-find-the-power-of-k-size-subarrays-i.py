class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = [-1]*(len(nums)-k+1)
        q = deque()
        maxVal = -float('inf')
        maxIdx = None
        counter = 0
        for r in range(len(nums)):
            curr = nums[r]
            """
            if q and curr != q[-1]+1:
                q.clear()
            q.append(curr)
            """
            if maxIdx != None and curr != maxVal+1:
                maxVal = -float('inf')
                maxIdx = None
                counter = 0
            maxVal = nums[r]
            maxIdx = r
            counter += 1

            if counter == k:
                res[r-k+1] = maxVal
                counter -= 1
            """
            if len(q) == k:
                res[r-k+1] = q[-1]
                q.popleft()
            """
        return res

            
                

