class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        repeated = word
        while repeated in sequence:
            k += 1
            repeated += word  # Concatenate word again
        return k
            
