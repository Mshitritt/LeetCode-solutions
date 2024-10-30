class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        j = sorted(jobs, reverse=True)
        w = sorted(workers, reverse=True)

        days = 0
        if w[0] >= j[0]:
            days = 1
        else:
            d = j[0] // w[0]
            if w[0]*d == j[0]:
                days += d
            else:
                days += d + 1

        for i in range(1, len(jobs)):
            if w[i] < j[i]:
                d = j[i] // w[i]
                if w[i]*d != j[i]:
                    d += 1
                days = max(days, d)
        return days