class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        freq = Counter(nums)
        keys = freq.keys()
        
        def rec():
            if len(nums) == len(perm):
                res.append(perm.copy())
                return

            for k in keys:
                if freq[k] > 0:
                    perm.append(k)
                    freq[k] -= 1

                    rec()

                    freq[k] += 1
                    perm.pop()
        rec()
        return res
        
        ans = rec(nums)
        return ans

