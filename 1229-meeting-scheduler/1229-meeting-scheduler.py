class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # GPT version of my solution below 
        slots1.sort()
        slots2.sort()
        
        i1, i2 = 0, 0

        while i1 < len(slots1) and i2 < len(slots2):
            s1, e1 = slots1[i1]
            s2, e2 = slots2[i2]

            # Calculate the overlap
            start = max(s1, s2)
            end = min(e1, e2)

            # Check if overlap is sufficient for the meeting duration
            if end - start >= duration:
                return [start, start + duration]

            # Advance the pointer for the interval that ends first
            if e1 < e2:
                i1 += 1
            else:
                i2 += 1

        return []
        """
        slots1.sort()
        slots2.sort()
        i1, n1 = 0, len(slots1)
        i2, n2 = 0, len(slots2)
        res = []

        
        while i1 < n1 and i2 < n2:
            s1, e1 = slots1[i1]
            s2, e2 = slots2[i2]

            # case no intersection 
            while (i1 < n1 and e1 <= s2):
                i1 += 1
                if i1 == n1:
                    break
                else:
                    s1, e1 = slots1[i1]
            
            while (i2 < n2 and e2 <= s1):
                i2 += 1
                if i2 == n2:
                    break
                else:
                    s2, e2 = slots2[i2]
            
            if i1 == n1 or i2 == n2:
                return res
            
            # case have intersection 
            s1, e1 = slots1[i1]
            s2, e2 = slots2[i2]

            
            newS = max(s1, s2)
            newE = min(e1, e2)

            if newE - newS >= duration:
                # have intersection 
                return [newS, newS+duration]
            else:
                # edge case - intersection slot small then duretion 
                if e1 < e2:
                    i1 += 1
                else:
                    i2 += 1


        return []
        """ 
            
