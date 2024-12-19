class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i1, n1 = 0, len(firstList)
        i2, n2 = 0, len(secondList)

        while i1 < n1 and i2 < n2:
            s1, e1 = firstList[i1]
            s2, e2 = secondList[i2]

            if s1 <= s2 <= e1 or s2 <= s1 <= e2:
                # overlapping
                newS = max(s1, s2)
                newE = min(e1, e2)
                res.append([newS, newE])

            
            if s1 < s2:
                if i1 == n1-1:
                    i2 += 1
                else:
                    i1 += 1
            else:
                if i2 == n2-1:
                    i1 += 1
                else:
                    i2 += 1


        return res


        