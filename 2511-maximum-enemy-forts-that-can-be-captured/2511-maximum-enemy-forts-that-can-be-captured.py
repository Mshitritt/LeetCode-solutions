class Solution:
    def captureForts(self, forts: List[int]) -> int:
        l = 0 
        r = l + 1
        captures = 0
        # edge case - empty, one element 
        while r < len(forts):
            tempCaptures = 0
            if forts[l] == 1:
                # tempCaptures = 0
                while r < len(forts) and forts[r] == 0:
                    tempCaptures += 1
                    r += 1
                if r < len(forts) and forts[r] == -1:
                    captures = max(tempCaptures, captures)
                l = r
                r = l + 1
            elif forts[l] == -1:
                # tempCaptures = 0
                while r < len(forts) and forts[r] == 0:
                    tempCaptures += 1
                    r += 1
                if r < len(forts) and forts[r] == 1:
                    captures = max(tempCaptures, captures)
                l = r
                r = l + 1
            else:
                l += 1
                r = l + 1
        return captures



