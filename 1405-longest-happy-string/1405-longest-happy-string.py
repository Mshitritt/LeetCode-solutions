class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        letters = []    #(freq, char, lst_idx)
        if a:
            heapq.heappush(letters, (-a, 'a'))
        if b:
            heapq.heappush(letters, (-b, 'b'))
        if c:
            heapq.heappush(letters, (-c, 'c'))
        
        res = []
        count = 1

        while letters:
            freq, char = heapq.heappop(letters)
            if res and res[-1] == char:
                count += 1
            else:
                count = 1
            if count == 3:
                if letters:
                    freq2, char2 = heapq.heappop(letters)
                    res.append(char2)
                    freq2 += 1
                    if freq2:
                        heapq.heappush(letters, (freq2, char2))
                    count = 1
                else:
                    break
            res.append(char)
            freq += 1
            if freq:
                heapq.heappush(letters, (freq, char))
        
        resFinal = ""
        for l in res:
            resFinal += l
        return resFinal



