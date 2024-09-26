class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the complement and its index
        num_to_index = {}

        # Iterate through the list of numbers
        for idx, val in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - val

            # If the complement exists in the dictionary, return the indices
            if complement in num_to_index:
                return [num_to_index[complement], idx]
            
            # Store the current value and its index in the dictionary
            num_to_index[val] = idx

        # Return an empty list if no solution is found (shouldn't happen if valid input)
        return []

        