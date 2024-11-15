class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # Step 1: Create a boolean array of size 51 to mark coverage
        covered = [False] * 51

        # Step 2: Mark the numbers covered by each interval in ranges
        for start, end in ranges:
            for num in range(start, end + 1):
                covered[num] = True

        # Step 3: Check if all numbers from left to right are covered
        for num in range(left, right + 1):
            if not covered[num]:
                return False

        return True