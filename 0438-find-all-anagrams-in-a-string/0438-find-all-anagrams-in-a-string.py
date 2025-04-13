class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return 0
        pfreq = Counter(p)
        lp = len(p)
        sfreq = defaultdict(int)
        res = []

        for r in range(len(s)):
            sfreq[s[r]] += 1
            
            if r >= lp:
                sfreq[s[r-lp]] -= 1
                if not sfreq[s[r-lp]]:
                    del sfreq[s[r-lp]]
            if sfreq == pfreq:
                res.append(r - lp + 1)
        
        return res
            