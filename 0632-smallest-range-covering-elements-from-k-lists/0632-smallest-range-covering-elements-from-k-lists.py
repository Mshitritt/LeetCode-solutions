class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minVal = float('inf')
        maxVal = -float('inf')
        heap = []
        k = len(nums)
        n = len(nums[0])    # length of shortest list
        for num in nums:
            n = min(n, len(num))
        
        
        # initianlaize 
        for li in range(k):
            item = (nums[li][0], li, 0)
            heapq.heappush(heap, item)  #(val, (list, idx)) 
            maxVal = max(maxVal, nums[li][0])
        minVal = heap[0][0]
        
        start, end = minVal, maxVal
        while True:
            prev = heapq.heappop(heap)
            prevVal, prevList, prevIdx = prev[0], prev[1], prev[2]
            if prevIdx+1 < len(nums[prevList]):
                item = (nums[prevList][prevIdx+1], prevList, prevIdx+1)
                heapq.heappush(heap, item)  #(val, (list, idx))
                curr = heap[0]
                currVal, currList, currIdx = curr[0], curr[1], curr[2]
                start = currVal
                end = max(end, nums[prevList][prevIdx+1])

                # save minimum range
                if end-start < maxVal-minVal:
                    minVal = start
                    maxVal = end
            else:
                return [minVal, maxVal]



            






            