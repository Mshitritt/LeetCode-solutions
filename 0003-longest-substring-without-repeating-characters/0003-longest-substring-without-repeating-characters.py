class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        abctadef
        """
        left = 0
        right = 1
        while right < len(s):
            curr = set(s[left: right])
            if len(curr) == right - left:
                # curr is substring
                if s[right] not in curr:
                    right += 1
                else:
                    right += 1
                    left += 1
            else:
                right += 1
                left += 1
        return right - left
        