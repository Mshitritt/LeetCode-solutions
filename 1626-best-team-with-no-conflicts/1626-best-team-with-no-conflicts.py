class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = []
        for a, s in zip(ages, scores):
            players.append((a, s))
        
        players.sort()
        dp = [players[i][1] for i in range(len(players))]
        
        res = max(dp)
        for i in range(1, len(players)):
            for j in range(i):
                if players[j][0] < players[i][0] and players[j][1] > players[i][1]:
                    # conflict
                    continue
                else:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
                    res = max(res, dp[i])
        return res