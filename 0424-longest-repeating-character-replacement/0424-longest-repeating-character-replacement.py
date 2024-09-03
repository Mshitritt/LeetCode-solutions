from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # calculate number of changes
        l = 0
        r = 0
        freq = {}
        most_freq = 0
        max_len = 0

        while r < len(s):
            # Count frequency of each element
            freq[s[r]] = freq.get(s[r], 0) + 1
            # Update the most frequent character count in the current window
            most_freq = max(most_freq, freq[s[r]])

            # Calculate changes needed
            window = r - l + 1
            curr_changes = window - most_freq

            if curr_changes > k:
                freq[s[l]] -= 1
                l += 1

            # Update the maximum length of the valid window
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len

