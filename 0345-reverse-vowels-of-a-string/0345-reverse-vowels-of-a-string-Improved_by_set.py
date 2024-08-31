class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')  # Using a set for fast lookup

        left, right = 0, len(s) - 1
        lst = list(s)

        while left < right:
            if lst[left] in vowels and lst[right] in vowels:
                lst[left], lst[right] = lst[right], lst[left]  # Swap vowels
                left += 1
                right -= 1
            elif lst[left] not in vowels:  # Move left pointer if not a vowel
                left += 1
            else:  # Move right pointer if not a vowel
                right -= 1
            
        return ''.join(lst)
