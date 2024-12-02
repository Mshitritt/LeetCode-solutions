class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        perm = []
        res = []
        def rec(i):
            nonlocal perm
            nonlocal res
            if len(perm) == k:
                res.append(perm.copy())
                return
            if i > n:
                return

            perm.append(i)
            rec(i+1)
            perm.pop()
            rec(i+1)
            
            return res
        return rec(1)