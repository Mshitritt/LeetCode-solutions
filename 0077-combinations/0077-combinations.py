class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        perm = []
        res = []
        def rec(i):
            
            if len(perm) == k:
                res.append(perm.copy())
                return
            if i > n:
                return

            perm.append(i)
            rec(i+1)
            perm.pop()
            rec(i+1)
            
            
        rec(1)
        return res