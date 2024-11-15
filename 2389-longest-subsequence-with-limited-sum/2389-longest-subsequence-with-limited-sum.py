class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        # search for lower closest prefix of num
        def search(num):
            l = 0
            r = len(prefix)-1
            while l <= r:
                mid = (l + r) // 2
                
                if prefix[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        res = [search(num) for num in queries]
        return res

