class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            res = []
            i1, i2 = 0, 0
            while i1 < len(arr1) and i2 < len(arr2):
                if arr1[i1] <= arr2[i2]:
                    res.append(arr1[i1])
                    i1 += 1
                else:
                    res.append(arr2[i2])
                    i2 += 1
                
            res.extend(arr1[i1:])
            res.extend(arr2[i2:])
            
                    
            return res
        
        def mergeRec(s, e):
            if e-s+1 == 1:
                return [nums[s]]
            m = s + (e - s) // 2
            left = mergeRec(s, m)
            right = mergeRec(m+1, e)

            return merge(left, right)
        
        return mergeRec(0, len(nums)-1)
