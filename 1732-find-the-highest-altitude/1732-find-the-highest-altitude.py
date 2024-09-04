class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        alt = 0
        for i in range(len(gain)):
            
            curr_alt = curr_alt + gain[i]
            alt = max(alt, curr_alt)
        return alt