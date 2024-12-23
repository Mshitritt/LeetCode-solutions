class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        heap = []

        # Step 1: Push the first element of each subarray into the heap
        for i in range(n):
            heapq.heappush(heap, (nums[i], i, nums[i]))  # (current_sum, start_index, next_value)

        res = 0

        # Step 2: Extract the smallest sums from the heap for indices `left` to `right`
        for _ in range(right):
            current_sum, start_index, next_value = heapq.heappop(heap)

            # Only add to result if we're within the range [left, right]
            if left <= 1:
                res = (res + current_sum) % MOD
            else:
                left -= 1

            # Push the next sum for this subarray into the heap
            if start_index + 1 < n:
                heapq.heappush(heap, (current_sum + nums[start_index + 1], start_index + 1, nums[start_index + 1]))

        return res