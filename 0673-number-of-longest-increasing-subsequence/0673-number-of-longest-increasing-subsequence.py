class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Coordinate compression: map each unique value to a unique index starting at 1.
        sorted_vals = sorted(set(nums))
        comp = {val: i + 1 for i, val in enumerate(sorted_vals)}
        m = len(sorted_vals)

        # BIT: each element stores a pair (length, count)
        BIT = [(0, 0)] * (m + 1)

        def combine(pair1, pair2):
            # Combine two (length, count) pairs:
            # - Return the one with the larger length.
            # - If lengths are equal, sum the counts.
            if pair1[0] > pair2[0]:
                return pair1
            elif pair1[0] < pair2[0]:
                return pair2
            else:
                return (pair1[0], pair1[1] + pair2[1])
        
        def update(idx, new_pair):
            # Update BIT at index idx with new_pair and all relevant ancestors.
            while idx <= m:
                BIT[idx] = combine(BIT[idx], new_pair)
                idx += idx & -idx

        def query(idx):
            # Query BIT for the combined (length, count) pair in range [1, idx]
            res = (0, 0)
            while idx:
                res = combine(res, BIT[idx])
                idx -= idx & -idx
            return res

        # Process each number in the input list.
        for num in nums:
            pos = comp[num]  # compressed coordinate
            best = query(pos - 1)  # best result for values strictly less than num

            # If no valid subsequence is found, start a new subsequence of length 1.
            if best[0] == 0:
                new_pair = (1, 1)
            else:
                new_pair = (best[0] + 1, best[1])
            update(pos, new_pair)

        # Final query over the entire BIT returns the best overall (length, count)
        overall = query(m)
        return overall[1]

        
