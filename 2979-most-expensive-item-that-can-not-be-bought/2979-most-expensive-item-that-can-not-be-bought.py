class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        """
        can buy z if exist x, y such as x*primeOne + y*primeTwo = z

        - if one of primes is 2 so the seconde is odd 
            --> the item is lower from prime's numbers 
        - if 
        """
        if primeOne == 2 or primeTwo == 2:
            return abs(primeOne - primeTwo)
        else:
            return primeOne*primeTwo - primeOne - primeTwo