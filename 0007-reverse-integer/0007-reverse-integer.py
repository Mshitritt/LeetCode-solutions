class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        num = x

        if x < 0:
            negative = True
            num = num * -1
        
        num_str = str(num)
        n = len(num_str)-1
        newNum = 0
        for i in range(-1, -n-2, -1):
            digit = int(num_str[i])
            p = pow(10, n)
            newNum += p * digit
            n -= 1

        if negative:
            newNum = -newNum

        lowest = -pow(2, 31)
        highest = pow(2, 31)-1
        if newNum < lowest or newNum > highest:
            return 0
        
        return newNum

        
        