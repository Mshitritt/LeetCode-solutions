class Solution:
    from functools import cmp_to_key
    def largestNumber(self, nums: List[int]) -> str:
        def comparing(e1, e2):
            if e1 + e2 > e2 + e1:
                # e1 is bigger or equal to e2
                return -1
            elif e1 + e2 < e2 + e1:
                # e2 is bigger 
                return 1
            else:
                return 0 
        
        #nums_str = str(nums)
        nums_str = list(map(str, nums))
        nums_sorted = sorted(nums_str, key=cmp_to_key(comparing))
        res_str = ''.join(nums_sorted)
        res = int(res_str)

        return str(res)


            
