class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        My solution act like merge sort, so the running time --> O(nlogn)
        But I map each num many times --> we map the nums once and than run the algorithem
        """
        
        n = len(nums)
        numsMapped = []

        for i in range(n):
            num = str(nums[i])
            key = ""
            for d in num:
                key += str(mapping[int(d)])
            
            numsMapped.append((key, i))
        
        numsMapped.sort()   # sort by key and than by index
        res = []

        for _, i in numsMapped:
            res.append(int(nums[i]))

        return res
            



        
        
        
        
        
        
        
        
        
        """
        # Time Limit Exceeded - O(nlogn)
        def getKey(num):
            mapped_str = "".join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_str)
        
        def rec(s, e):
            if e - s + 1 == 1:
                return [nums[s]]
            
            mid = (s + e) // 2
            left = rec(s, mid)
            right = rec(mid + 1, e)

            # merge
            res = []
            il, ir = 0, 0
            while il < len(left) and ir < len(right):
                leftKey, rightKey = getKey(left[il]), getKey(right[ir])
                if leftKey <= rightKey:
                    res.append(left[il])
                    il += 1
                else:
                    res.append(right[ir])
                    ir += 1
            
            while il < len(left):
                res.append(left[il])
                il += 1
            while ir < len(right):
                res.append(right[ir])
                ir += 1
            
            return res

        return rec(0, len(nums)-1)
        """
        
        

