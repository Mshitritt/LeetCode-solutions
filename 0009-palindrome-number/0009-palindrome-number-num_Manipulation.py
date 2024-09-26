class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            # Build the reversed number one digit at a time
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # If the original number is a palindrome, the first half should equal the second half
        # For odd-length numbers, we can ignore the middle digit by reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

