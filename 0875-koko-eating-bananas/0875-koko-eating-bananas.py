class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        - the minum k should be equal or grat than sum(piles)//h 
        - the maximum k is the largest piles[i]
        """
        def get_hours(piles, k):
            hourse = 0
            for pile in piles:
                hourse += (pile + k - 1) // k
            return hourse

        
        high = max(piles)
        low = 1

        k = 0
        while low <= high:
            # possible k
            mid = (low + high) // 2
            mid_hours = get_hours(piles, mid)
            if mid_hours <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
                



