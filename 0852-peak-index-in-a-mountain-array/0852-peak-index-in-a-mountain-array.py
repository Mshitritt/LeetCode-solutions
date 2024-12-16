class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l <= r:
            mid = (l+r)//2
            if mid == 0:
                if arr[mid] > arr[mid+1]:
                    return mid
                else:
                    l = mid+1
            elif mid == len(arr)-1:
                if arr[mid] > arr[mid-1]:
                    return mid
                else:
                    r = mid-1
            elif arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]:
                return mid
            elif arr[mid-1] <= arr[mid] <= arr[mid+1]:
                # on increase side
                l = mid+1
            else:
                r = mid-1
        return -1
