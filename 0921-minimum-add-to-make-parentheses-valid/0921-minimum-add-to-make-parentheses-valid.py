class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens = 0
        closes = 0
        for c in s:
            if c == "(":
                opens += 1
            else:
                if opens:
                    opens -= 1
                else:
                    closes += 1
        return abs(opens) + abs(closes)