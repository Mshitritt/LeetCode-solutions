class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        while i < n-1:
            if arr[i] == 0:
                s = arr[i + 1:n - 1]
                arr[i + 1] = 0
                arr[i + 2:] = s
                i += 2
            else:
                i += 1
        return None

        