class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groupLs = []
        tempLs = []
        
        while groupSizes:
            minGroup = min(groupSizes)
            if minGroup == float('inf'):
                return groupLs
            minGroup_copy = minGroup
            while minGroup_copy:
                iNum = groupSizes.index(minGroup)
                tempLs.append(iNum)
                groupSizes[iNum] = float('inf')
                minGroup_copy -= 1

            groupLs.append(tempLs)
            tempLs = []
        return groupLs



        