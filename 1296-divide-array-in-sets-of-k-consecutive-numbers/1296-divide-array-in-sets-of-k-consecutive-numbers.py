class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        freq = Counter(nums)
        start = min(freq.keys())

        while freq:
            size = k
            curr = start

            while size:
                if curr not in freq:
                    return False
                freq[curr] -= 1
                if not freq[curr]:
                    del freq[curr]
                size -= 1
                curr += 1
            
            while freq and start not in freq:
                start += 1
        return True
