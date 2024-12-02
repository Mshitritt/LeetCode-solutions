class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates = sorted(candidates)
        
        def rec(idx, total):
            if total == target:
                res.append(comb.copy())
                return
            if total > target or idx >= len(candidates):
                return

            comb.append(candidates[idx])
            rec(idx+1, total+candidates[idx])
            comb.pop()
            
            
            
            # Skip duplicates by moving to the next unique candidate
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            rec(idx + 1, total)

            
            
        rec(0, 0)
        return res

            



        