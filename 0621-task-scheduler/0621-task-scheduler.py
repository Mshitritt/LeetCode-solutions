class Solution:
    import heapq
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks).most_common()
        max_freq_value = freq[0][1]
        max_freq_count = 0
        for key, value in freq:
            if value == max_freq_value:
                max_freq_count += 1
        calc = (max_freq_value-1)*(n+1) + max_freq_count
        return max(calc, len(tasks))
        

        



        

        