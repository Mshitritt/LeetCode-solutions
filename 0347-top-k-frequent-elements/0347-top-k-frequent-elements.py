class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        freq = Counter(nums).most_common()
        res = []
        while k:
            c = freq[0][0]
            res.append(c)
            freq.pop(0)
            k -= 1
        return res

