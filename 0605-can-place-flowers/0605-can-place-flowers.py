class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if n == 1 and flowerbed[0] == 0:
                return True
            return False
        i = 0
        while i < len(flowerbed):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 0
                i += 2
            elif i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                n -= 1
                i += 2
            else:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                    i += 2
                else:
                    i += 1
        return n <= 0
        