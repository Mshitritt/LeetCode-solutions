class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        prefix, odd, even = 0, 0, 1
        res = 0
        for num in arr:
            prefix += num
            if prefix % 2:
                # prefix is odd --> remove even
                res += even % MOD
                odd += 1
            else:
                # prefix is even --> remove odd
                res += odd % MOD
                even += 1
        return res % MOD