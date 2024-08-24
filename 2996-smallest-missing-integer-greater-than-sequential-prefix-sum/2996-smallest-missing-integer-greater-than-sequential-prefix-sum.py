class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Missing edge case:
        nums1 = [1, 2, 3, 2, 5] --> output 6 is correct
        nums2 = [46, 1, 2, 3] --> output 46 is wrong since nums2 includes 46
        so you need to check if the sum of sequencd numers not include in nums
        """
        seqSum = nums[0]
        endSeqIndex = 0
        forbidden = []
        for i in range(1, len(nums)):
            # find the sequence numbers 
            if nums[i] == nums[i-1] + 1:
                seqSum += nums[i]
            else:
                # we have the sequence numbers 
                endSeqIndex = i
                break

        # case of 1 element in sequence numbers 
        numsRest = nums[endSeqIndex:]
        if len(numsRest) == len(nums)-1:
            seqSum += 1
            
        while numsRest:
            m = min(numsRest)
            M = max(numsRest)
            if seqSum > M:
                return seqSum
            elif seqSum == m:
                seqSum += 1
                numsRest.remove(m)
            else:
                numsRest.remove(m)


        return seqSum
                
        
            

        
        