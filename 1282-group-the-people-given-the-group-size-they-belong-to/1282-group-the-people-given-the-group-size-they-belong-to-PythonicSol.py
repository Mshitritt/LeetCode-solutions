class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        # Pythonic solution 
        groupLs = []
        groupDic = {}
        """
        for i in range(len(groupSizes)):
            gSize = groupSizes[i]   # key
            person = i              # value
            if gSize in groupDic:
                groupDic[gSize].append(person)
            else:
                ls = []
                ls.append(person)
                groupDic[gSize] = ls
        """
        """
        Pythonic explanation:
            dictionary.setdefault(key, default=None)
            way to add a new pair of 'key: value' to dictionary or retrieve value of key
            
            value = my_dict.setdefault('c', 3)
                1. if the pair 'c: 3' exist in my_dic --> method return the value of 'a' key 
                2. if the pair 'c: 3' doesnt exist in my_dic --> method set the new pair and return the value of pair
        
            in our case:
            the method check if exist empty list
                if doesnt exist --> create a new one and set as value of size
                if exist --> the method return the list 
        """
        for i, size in enumerate(groupSizes):
            groupDic.setdefault(size, []).append(i)
        
        """
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
        """
        for key, people in groupDic.items():
            for i in range(0, len(people), key):
                groupLs.append(people[i:i + key])
        return groupLs



        