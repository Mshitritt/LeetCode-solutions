class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        count = [0] * 60  # count[i] = number of times we've seen remainder i
        res = 0

        for t in time:
            rem = t % 60
            complement = (60 - rem) % 60
            res += count[complement]
            count[rem] += 1

        return res
        

            

                