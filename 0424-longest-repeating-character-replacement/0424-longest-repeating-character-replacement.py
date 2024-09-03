from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # calculate number of changes
        l = 0
        r = 0
        while r < len(s):
            window = r - l
            # count frequency of each element
            freq = dict(Counter(s[l:r + 1]))

            # find the most frequency char
            most_freq = 0
            for key in freq:
                most_freq = max(most_freq, freq[key])

            # calculate changes
            curr_changes = window - most_freq + 1

            if curr_changes > k:
                l += 1
                r += 1
            else:
                r += 1

        return r - l
