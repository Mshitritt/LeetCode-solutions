class Solution:
    def captureForts(self, forts: List[int]) -> int:
        maxCaptures = 0
        n = len(forts)
        i = 0
        
        while i < n:
            # Find the starting fort (either 1 or -1)
            if forts[i] == 1 or forts[i] == -1:
                startFort = forts[i]
                tempCaptures = 0
                j = i + 1
                
                # Check the next positions for zeros until a different fort is found
                while j < n and forts[j] == 0:
                    tempCaptures += 1
                    j += 1
                
                # If a different fort is found, update max captures
                if j < n and forts[j] == -startFort:
                    maxCaptures = max(maxCaptures, tempCaptures)
                
                # Move to the position after the current sequence
                i = j
            else:
                i += 1
        
        return maxCaptures



