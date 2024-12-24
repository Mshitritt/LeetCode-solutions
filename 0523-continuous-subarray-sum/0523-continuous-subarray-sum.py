class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0: -1}
        prefix = 0 

        for i, num in enumerate(nums):

            prefix = (prefix + num) % k
            if prefix in hash_map or prefix == 0:
                # Check if subarray length is at least 2
                if i - hash_map[prefix] > 1:
                    return True
            else:
                # Store the first occurrence of this prefix % k
                hash_map[prefix] = i
        return False