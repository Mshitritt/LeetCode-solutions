class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_len = 1
        n = len(nums)
        minQ = deque()  # Min deque to store values in increasing order
        maxQ = deque()  # Max deque to store values in decreasing order

        for right in range(n):
            while minQ and nums[right] < minQ[-1]:
                minQ.pop()
            minQ.append(nums[right])

            while maxQ and nums[right] > maxQ[-1]:
                maxQ.pop()
            maxQ.append(nums[right])

            # validation check
            while maxQ[0] - minQ[0] > limit:
                if nums[left] == maxQ[0]:
                    maxQ.popleft()
                if nums[left] == minQ[0]:
                    minQ.popleft()
                left += 1
            max_len = max(max_len, right-left+1)

        return max_len


                

        
