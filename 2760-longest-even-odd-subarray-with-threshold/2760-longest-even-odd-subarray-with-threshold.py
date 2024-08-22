class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        subArray = 0
        c = 0
        for l in range(len(nums)):
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                c = 1

                for r in range(l + 1, len(nums)):
                    """
                    code improvments: 
                    1. if there has a same condiation in all parts of ifs, like nums[r] <= threshold:
                        --> move it up and check it first 
                    2. if there has 2 opposide condition, like nums[r] % 2 == 1 and then nums[r-1] % 2 == 0
                        --> check if they are differents nums[r] % 2 != nums[r-1] % 2  
                    """
                    if nums[r] > threshold:
                        break 
                    if nums[r] % 2 == nums[r-1] % 2:
                        break
                    
                    c += 1
                """
                code improvements:
                3. use in Python build in function instead of implemnt your own,
                    if you want the bigger element of: A, B. 
                    DONT check it by yourselfe like: if A > B: bigger = A
                    Do use Python built in function: bigger = max(A, B)
                """
                subArray = max(subArray, c)

        return subArray
                        
                        





        