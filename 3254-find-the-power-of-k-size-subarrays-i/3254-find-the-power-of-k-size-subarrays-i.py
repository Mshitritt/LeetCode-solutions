class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = [-1]*(len(nums)-k+1)
        q = deque()

        for r in range(len(nums)):
            curr = nums[r]
            if q and curr != q[-1]+1:
                q.clear()
            q.append(curr)

            if len(q) == k:
                res[r-k+1] = q[-1]
                q.popleft()
        return res

            
                

