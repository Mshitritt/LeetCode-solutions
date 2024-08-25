import math
class Solution(object):
    def GCD(self, a, b):
        while b:
            a, b = b, a % b
        return a


    def gcd_multiple(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result = self.GCD(result, num)
        return result

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) == 0 or len(deck) == 1:
            return False
        gcd = []
        while deck:
            # count how many elements have for each unique value
            minVal = min(deck)
            countMin = deck.count(minVal)
            if countMin == 1:
                return False
            gcd.append(countMin)
            while countMin:
                deck.remove(minVal)
                countMin -= 1

            # calculate the GCD between groups
            # if GCD > 1 --> True
            # else --> return False
        result = self.gcd_multiple(gcd)

        if result > 1:
            return True
        return False