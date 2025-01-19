class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        maxVal, minVal = max(nums), min(nums)
        # edge case 
        if maxVal == minVal:
            return 0

        # find range for bucket 
        b = (maxVal - minVal)//(n-1)
        if b == 0:
            b += 1
        # find number of buckets 
        k = math.ceil((maxVal - minVal) / b) 

        # table to store bucket valuse 
        # bucket[i][0] - minValue
        # bucket[i][1] - maxValue
        bucket = [[-1, -1] for _ in range(k+1)]

        # allocate each number into bucket 
        for num in nums:
            idx = (num - minVal) // b

            minBuck, maxBuck = bucket[idx]
            if minBuck == maxBuck == -1:
                bucket[idx][0], bucket[idx][1] = num, num
            elif minBuck <= maxBuck < num:
                bucket[idx][1] = num
            elif num < minBuck <= maxBuck:
                bucket[idx][0] = num
        
        # compute max gap
        maxGap = 0
        prevBucket = 0
        while bucket[prevBucket] == [-1, -1]:
            prevBucket += 1
        currBucket = prevBucket + 1

        while currBucket < k:
            if bucket[currBucket] == [-1, -1]:
                currBucket += 1
            else:
                gap = bucket[currBucket][0] - bucket[prevBucket][1]
                maxGap = max(maxGap, gap)
                prevBucket = currBucket 
                currBucket += 1
        
        # check for maxValue 
        maxGap = max(maxGap, maxVal - bucket[prevBucket][1])
        return maxGap



    
        
        
