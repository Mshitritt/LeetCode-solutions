class Solution:
    def reorganizeString(self, s: str) -> str:
        # using in heap 
        frequency = Counter(s)
        sorted_counter = dict(frequency.most_common())
        keys = list(sorted_counter.keys())
        n = len(s)
        if sorted_counter[keys[0]] > (n + 1)//2:
            return ""

        res = ['0'] * n
        pos = 0
        for key in keys:
            while sorted_counter[key]:
                if pos >= n:
                    pos = 1
                sorted_counter[key] -= 1
                res[pos] = key
                pos += 2

        return "".join(res)
        
        