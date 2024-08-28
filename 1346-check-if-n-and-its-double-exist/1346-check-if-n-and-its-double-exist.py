class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return False
        arr.sort()
        # 2, 3, 5, 6, 7, 8

        for i in range(len(arr)):
            target = arr[i]*2
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = (high + low) // 2

                if arr[mid] == target and mid != i:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
                    

