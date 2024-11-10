class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        l = 0
        r = len(height)-1
        maxL = 0
        maxR = 0
        res = 0
        while l <= r:
            if maxL <= maxR:
                # move left
                water = maxL - height[l]
                res += max(water, 0)
                maxL = max(maxL, height[l])
                l += 1
            else:
                # right move
                water = maxR - height[r]
                res += max(water, 0)
                maxR = max(maxR, height[r])
                r -= 1
                
                    
        return res


            
            


