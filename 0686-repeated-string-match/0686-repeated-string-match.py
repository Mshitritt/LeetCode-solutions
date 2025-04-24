class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # lps on b
        m = len(b)
        lps = [0]*m
        i, j = 1, 0
        while i < m:
            if b[i] == b[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j-1]
        
        # KMP - match pattern 
        n = len(a)
        maxTimes = n + m
        i, j = 0, 0 # i for 'a', j for 'b'
        while i < maxTimes:
            idx = i % n
            if a[idx] == b[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == m:
                return math.ceil(i / n)
        return -1