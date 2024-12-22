class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = defaultdict(int)
        for f, t, a in transactions:
            debt[f] -= a
            debt[t] += a
        
        balance_list = [amount for amount in debt.values() if amount]
        n = len(balance_list)

        def dfs(cur):
            while cur < n and not balance_list[cur]:
                cur += 1
            if cur == n:
                return 0
            cost = float('inf')
            for nxt in range(cur + 1, n):
                # If nxt is a valid recipient, do the following: 
                # 1. add cur's balance to nxt.
                # 2. recursively call dfs(cur + 1).
                # 3. remove cur's balance from nxt.
                if balance_list[nxt] * balance_list[cur] < 0:
                    balance_list[nxt] += balance_list[cur]
                    cost = min(cost, 1 + dfs(cur + 1))
                    balance_list[nxt] -= balance_list[cur]
            return cost
        
        return dfs(0)




        