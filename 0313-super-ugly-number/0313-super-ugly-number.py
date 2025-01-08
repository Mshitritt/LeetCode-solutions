class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Use heap to efficiently get minimum value
        from heapq import heappush, heappop

        ugly = [1]
        heap = []
        
        # Initialize heap with first multiples
        for prime in primes:
            heappush(heap, (prime, prime, 0))  # (value, prime, index)
        
        # Generate n-1 more ugly numbers
        while len(ugly) < n:
            next_ugly, prime, index = heappop(heap)
            
            # Skip duplicates
            if next_ugly != ugly[-1]:
                ugly.append(next_ugly)
            
            # Push next multiple
            heappush(heap, (prime * ugly[index + 1], prime, index + 1))
        
        return ugly[-1]




