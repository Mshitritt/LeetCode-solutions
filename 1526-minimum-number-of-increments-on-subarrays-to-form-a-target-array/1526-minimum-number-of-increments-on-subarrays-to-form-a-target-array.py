class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = target[0]  # Initialize with the first value
        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                operations += target[i] - target[i-1]
        return operations
                    

                


        

