class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        majorItem = nums[0]
        majorAmount = frequency[nums[0]]
        for key in frequency:
            if frequency[key] >= majorAmount:
                majorAmount = frequency[key]
                majorItem = key

        return majorItem
