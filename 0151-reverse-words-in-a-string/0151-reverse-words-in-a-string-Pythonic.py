class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by whitespace and filter out empty strings
        words = s.split()
        
        # Reverse the list of words
        words.reverse()
        
        # Join the reversed list with a single space
        return ' '.join(words)
        