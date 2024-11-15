class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count = [0]*101
        prefix = [0]*101

        for birth, death in logs:
            b = birth - 1950
            d = death - 1950
            count[b] += 1
            count[d] -= 1

        maxPop = 0
        maxIdx = 0
        for i in range(1, 101):
            prefix[i] = prefix[i-1] + count[i]
            if prefix[i] > maxPop:
                maxPop = prefix[i]
                maxIdx = i
        
        return maxIdx + 1950


