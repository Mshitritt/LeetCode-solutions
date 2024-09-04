class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        prefix_sum = [0]*(n + 1)
        alt = 0
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + gain[i-1]
            alt = max(alt, prefix_sum[i])
        return alt