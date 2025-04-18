class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def valid(d):
            return len(set(d.values())) == 1 

        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 characters = 0 partitions

        for i in range(1, n + 1):  # End index
            freq = defaultdict(int)
            for j in range(i, 0, -1):  # Start index, reverse to reuse freq
                freq[s[j - 1]] += 1
                if valid(freq):
                    dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n]




