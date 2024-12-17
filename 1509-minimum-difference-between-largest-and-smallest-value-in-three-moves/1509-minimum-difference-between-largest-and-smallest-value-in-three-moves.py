class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0

        
        res = float('inf')
        maxHeap = []    # store maximum elements from **small -> large**
        minHeap = []    # store minimum elements from **large -> small**
        
        for num in nums:
            if len(maxHeap) < 4:
                heapq.heappush(maxHeap, num)
                heapq.heappush(minHeap, -num)
            else:
                if num >= maxHeap[0]:
                    heapq.heappushpop(maxHeap, num)
                if -num >= minHeap[0]:
                    heapq.heappushpop(minHeap, -num)
        
        minHeap = sorted([-x for x in minHeap])
        maxHeap = sorted([x for x in maxHeap], reverse=True)
        for i in range(4):
            res = min(res, maxHeap[3-i] - minHeap[i]) 
        # op1 = nums[-4] - nums[0]    # 3 larget
        # op3 = nums[-3] - nums[1]    # 2 largest, 1 smallest
        # op4 = nums[-2] - nums[2]    # 1 largest, 2 smallest
        # op2 = nums[-1] - nums[3]    # 3 smallest
        return res
        