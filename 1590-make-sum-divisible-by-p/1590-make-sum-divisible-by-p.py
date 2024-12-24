class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0

        mod_map = {0: -1}  # Maps prefix modulo to index
        prefix_sum = 0
        min_len = float('inf')

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            # Calculate the modulo needed to achieve the target
            needed_mod = (prefix_sum - target) % p
            
            # Check if the needed modulo exists in the map
            if needed_mod in mod_map:
                min_len = min(min_len, i - mod_map[needed_mod])
            
            # Update the map with the current prefix modulo
            mod_map[prefix_sum] = i

        return min_len if min_len < len(nums) else -1

        

                


        

        

