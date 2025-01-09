class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        counter = {}
        counter[(0, 0, 0, 0, 0)] = -1
        mask = [0, 0, 0, 0, 0]  # [a, e, i, o, u]
        res = 0
        for i, char in enumerate(s):
            # update mask
            if char in "aeiou":
                if char == 'a':
                    mask[0] = (mask[0] + 1) % 2
                if char == 'e':
                    mask[1] = (mask[1] + 1) % 2
                if char == 'i':
                    mask[2] = (mask[2] + 1) % 2
                if char == 'o':
                    mask[3] = (mask[3] + 1) % 2
                if char == 'u':
                    mask[4] = (mask[4] + 1) % 2

            # calculate the longest substring
            bitmask = tuple(mask)
            if bitmask in counter:
                j = counter[bitmask]
                res = max(res, i-j)
            else:
                counter[bitmask] = i
        return res