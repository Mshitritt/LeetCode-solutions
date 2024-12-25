class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        prefix = [0]*len(arr)
        prefix[0] = arr[0]
        for i in range(1, k):
            prefix[i] = prefix[i-1] + arr[i]
        
        # check first subarray 
        avg = prefix[k-1] / k
        res += 1 if avg >= threshold else 0

        
        for i in range(k, len(arr)):
            prefix[i] = prefix[i-1] + arr[i]
            total = prefix[i] - prefix[i-k]
            avg = total / k
            res += 1 if avg >= threshold else 0
        return res
