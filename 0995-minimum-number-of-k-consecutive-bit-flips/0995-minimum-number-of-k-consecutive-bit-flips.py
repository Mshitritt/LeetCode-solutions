class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0  # Total flips needed
        flip = 0  # Current flip state
        flip_queue = deque()  # Queue to track active flip ranges

        for i in range(n):
            # Check if the current flip window ends at i
            if flip_queue and flip_queue[0] == i:
                flip_queue.popleft()
                flip ^= 1  # Deactivate the flip state

            # Check if nums[i] needs flipping
            if nums[i] ^ flip == 0:
                # Not enough elements remaining to flip
                if i + k > n:
                    return -1

                # Add a new flip starting at i
                flip_queue.append(i + k)
                flip ^= 1  # Toggle the flip state
                flips += 1

        return flips
