class Solution:
    def removeStars(self, s: str) -> str:
        stuck = []
        for c in s:
            if c != '*':
                stuck.append(c)
            else:
                if stuck:
                    stuck.pop()
        new_s = "".join(stuck)
        return new_s
