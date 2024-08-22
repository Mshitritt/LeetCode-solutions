class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        c = 0   # maximum available places 
        n_flowerbed = len(flowerbed)    # size of flowers array 

        while i < n_flowerbed:
            if i+1 < n_flowerbed:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    c += 1
                    i += 2
                elif flowerbed[i] == 1:
                    i += 2
                else:
                    i += 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    c += 1
                    break
                else:
                    break

        if n <= c:
            return True
        else:
            return False

        