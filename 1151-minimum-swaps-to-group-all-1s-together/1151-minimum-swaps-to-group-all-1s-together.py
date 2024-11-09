class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        zeros = ones - sum(data[:ones])
        r = ones
        res = zeros
        while r < len(data):
            if data[r - ones] == 0:
                zeros -= 1
            if data[r] == 0:
                zeros += 1
            res = min(res, zeros)
            r += 1
        return res

            
                

