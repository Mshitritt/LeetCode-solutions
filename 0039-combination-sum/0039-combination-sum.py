class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        dp = [[0 for _ in range(target+1)] for _ in range(n)]

        # initionlaize 
        for r in range(n):
            dp[r][0] = 1
        
        # fill dp table
        for i, can in enumerate(candidates):
            for t in range(1, target+1):
                if i == 0:
                    if t-can >= 0:
                        dp[i][t] += dp[i][t-can]
                else:
                    if t-can >= 0:
                        dp[i][t] += dp[i-1][t] + dp[i][t-can]
                    else:
                        dp[i][t] += dp[i-1][t]

        print([0, 1, 2, 3, 4, 5, 6, 7])
        print("---------------------------")
        for r in dp:
            print(r)
        
        # restore solution from dp 

        # Function to backtrack and restore combinations
        def backtrack(i, t):
            if t == 0:
                return [[]]  # Base case: one valid combination is found
            if i < 0:
                return []  # No combinations possible

            combinations = []
            
            # Option 1: Include candidates[i] if possible
            if t - candidates[i] >= 0 and dp[i][t - candidates[i]] > 0:
                for comb in backtrack(i, t - candidates[i]):  # Stay at the same `i` for reuse
                    combinations.append(comb + [candidates[i]])

            # Option 2: Exclude candidates[i] and move to the previous row
            if i > 0 and dp[i - 1][t] > 0:
                combinations.extend(backtrack(i - 1, t))
            
            return combinations
        
        # Start backtracking from the last cell
        return backtrack(n - 1, target)




        
        