class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        first, second = pattern
        count_first = 0  # Count occurrences of pattern[0]
        count_second = 0  # Count occurrences of pattern[1]
        count_subsequences = 0  # Count of "pattern" as a subsequence

        # Count occurrences of pattern[0] and pattern[1] and subsequences
        for char in text:
            if char == second: 
                count_subsequences += count_first  # Every pattern[0] before pattern[1] forms a subsequence
                count_second += 1
            if char == first:
                count_first += 1
        
        # Best placement: Add pattern[0] at the beginning OR pattern[1] at the end
        return count_subsequences + max(count_first, count_second)
            
