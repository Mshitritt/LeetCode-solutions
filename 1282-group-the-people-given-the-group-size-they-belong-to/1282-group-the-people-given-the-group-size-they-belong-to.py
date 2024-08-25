class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groupLs = []
        groupDic = {}
        for i in range(len(groupSizes)):
            gSize = groupSizes[i]   # key
            person = i              # value
            if gSize in groupDic:
                groupDic[gSize].append(person)
            else:
                ls = []
                ls.append(person)
                groupDic[gSize] = ls

        for key in groupDic:
            ls_g = []
            size = key
            for i in groupDic[key]:
                if size:
                    ls_g.append(i)
                    size -= 1
                else:
                    groupLs.append(ls_g)
                    ls_g = []
                    ls_g.append(i)
                    size = key-1
            groupLs.append(ls_g)

        return groupLs



        