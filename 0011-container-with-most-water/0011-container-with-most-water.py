class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        water = 0
        while l < r:
            high = min(height[l], height[r])
            width = r - l
            water = max(water, high * width)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return water
