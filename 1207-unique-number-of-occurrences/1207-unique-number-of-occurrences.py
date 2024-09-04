class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for num in arr:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        dic = dict(sorted(dic.items(), key=lambda item: item[1]))
        keys = list(dic.keys())
        for i in range(1, len(keys)):
            curr_key = keys[i]
            prev_key = keys[i-1]
            if dic[curr_key] == dic[prev_key]:
                return False
        return True