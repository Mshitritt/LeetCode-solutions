class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        w1 = abcde --> be
        w2 = aecdb --> eb

        w1 = aacabb --> aaabb
        w2 = bbcbaa --> bbbaa

        """
        if len(word1) != len(word2):
            return False

        d1 = list(word1)
        d2 = list(word2)

        d1.sort()
        d2.sort()
        if d1 == d2:
            return True

        s1 = set(d1)
        s2 = set(d2)
        if s1 != s2:
            return False
        else:
            a = list(Counter(d1).values())
            a.sort()
            b = list(Counter(d2).values())
            b.sort()
            if a == b:
                return True
        return False