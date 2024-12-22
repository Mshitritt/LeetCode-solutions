class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        wait = 0
        finish = customers[0][0]

        for arr, t in customers:
            wait = max(0, finish-arr)
            res += wait + t
            finish = arr + t + wait

        return res/len(customers)

            