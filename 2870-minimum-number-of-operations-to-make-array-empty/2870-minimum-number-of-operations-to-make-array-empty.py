class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        res = 0
        for num in nums:
            freq[num] += 1
        freq_val = list(freq.values())
        for num in freq_val:
            if num == 1:
                return -1 
            elif num%3 == 0:
                res += num//3
            else:
                # try combinations 
                max_three = num//3
                while max_three > -1:
                    remain = num - 3*max_three
                    if remain % 2 == 0:
                        res += max_three + (remain // 2)
                        break
                    else:
                        max_three -= 1
                if max_three < 0:
                    return -1
        return res
