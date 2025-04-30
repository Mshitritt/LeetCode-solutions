class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coins = {
            5: 0,
            10: 0,
            20: 0
        }

        for b in bills:
            coins[b] += 1
            # need return change
            change = b - 5
            if change:
                for c in [20, 10, 5]:
                    if 0 < c <= change:
                        while coins[c] and c <= change:
                            coins[c] -= 1
                            change -= c
            if change:
                return False
        return True

            