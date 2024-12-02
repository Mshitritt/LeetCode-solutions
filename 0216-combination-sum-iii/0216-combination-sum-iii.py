class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        comb = []
        if k > n:
            return res

        def rec(curr, total):
            
            if total == n and len(comb) == k:
                res.append(comb.copy())
                return
            if total > n or len(comb) > k or curr > 9:
                return

            # include curr 
            comb.append(curr)
            rec(curr+1, total+curr)

            # exclude curr
            comb.pop()
            rec(curr+1, total)

        rec(1, 0)
        return res

            


            
