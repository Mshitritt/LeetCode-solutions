import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        improve explanation:
        the old version using I use in split method (O(n)) inside of loop --> total complexity O(n^2)

        in this version we using in regular gcd finction from math
        """
        # Check if str1 + str2 == str2 + str1; if not, there's no common divisor
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the greatest common divisor of the lengths of str1 and str2
        gcd_len = math.gcd(len(str1), len(str2))
        
        # The largest common divisor string would be the prefix of length gcd_len of str1
        return str1[:gcd_len]


        

