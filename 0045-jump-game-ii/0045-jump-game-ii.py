class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0       # how many jumps
        max_pos = 0     # the farthest position we can reach with current jumps
        curr_end = 0    # the farthest position we can reach with index

        for i in range(n-1):
            max_pos = max(max_pos, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = max_pos
        
        return jumps


            