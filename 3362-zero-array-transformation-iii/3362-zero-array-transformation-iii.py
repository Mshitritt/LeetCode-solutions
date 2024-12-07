class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries = sorted(queries, key=lambda x: (x[0], x[1]))
        candidate = []
        chosen = []
        iq = 0
        res = 0
        for i in range(len(nums)):
            # get candidates 
            while iq < len(queries) and queries[iq][0] == i:
                l, r = queries[iq]
                heapq.heappush(candidate, (-r, l))
                iq += 1

            while chosen and chosen[0][0] < i:
                heapq.heappop(chosen)

            # chosen candidates
            if nums[i] != 0:
                amount = nums[i]
                
                amount -= len(chosen)
                while amount > 0 and candidate and -candidate[0][0] >= i:
                    curr = heapq.heappop(candidate)
                    r = -curr[0]
                    l = curr[1]
                    heapq.heappush(chosen, (r, l))
                    amount -= 1
                    res += 1
                if amount > 0:
                    return -1
        return len(queries)-res


                    

            

            