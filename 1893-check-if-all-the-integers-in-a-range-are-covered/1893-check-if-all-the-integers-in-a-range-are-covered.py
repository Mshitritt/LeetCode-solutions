class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            # Check if num is covered by any range in ranges
            covered = False
            for start, end in ranges:
                if start <= num <= end:
                    covered = True
                    break  # No need to check further ranges for this num
            if not covered:
                return False  # If any number is not covered, return False
        return True  # All numbers are covered