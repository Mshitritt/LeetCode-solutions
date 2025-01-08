class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = primes.copy()
        idx = [0]*len(primes)
        res = [1]*(n)

        for i in range(1, n):
            curr = min(uglies)
            res[i] = curr
            # states 
            for j, ugly in enumerate(uglies):
                if ugly == curr:
                    factor = primes[j]
                    idx[j] += 1
                    uglies[j] = res[idx[j]]*factor
        return res[n-1]





