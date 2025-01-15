class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        pos = True if num >= 0 else False
        if num < 0:
            num *= -1

        digits = []
        zeros = 0
        while num != 0:
            if num%10 == 0:
                zeros += 1
            else:
                digits.append(num%10)
            num //= 10
        
        if pos:
            digits.sort()
        else:
            digits.sort(reverse=True)
        
        newNum = digits[0]
        if zeros and pos:
            newNum *= 10**zeros
            

        for num in digits[1:]:
            newNum *= 10
            newNum += num
        if not pos:
            newNum = newNum * (10**zeros)
        return newNum if pos else -newNum
