class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        
       
        target = sum(nums) // k
        visited = [False] * len(nums)
        nums.sort(reverse=True)
        if total_sum % k != 0 or nums[0] > target:
            return False
            
        def rec(i, k_curr, total):
            if k_curr == 0:
                return True
            
            if total == target:
                return rec(0, k_curr-1, 0)

            for j in range(i, len(nums)):
                if visited[j] or total + nums[j] > target:
                    continue
                
                visited[j] = True
                if rec(j+1, k_curr, total+nums[j]):
                    return True
                visited[j] = False
            return False

        return rec(0, k, 0)
        
            

                