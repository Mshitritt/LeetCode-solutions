class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        abctadef
        """

        left = 0
        right = 0
        curr = set()
        while right < len(s):
            if s[right] not in curr and len(curr) == right - left:
                curr.add(s[right])
                right += 1
            else:
                left += 1
                right += 1
                curr = set(s[left: right])
        return right - left
        