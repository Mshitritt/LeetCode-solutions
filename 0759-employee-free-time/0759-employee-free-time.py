"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        sweep = defaultdict(int)
        for emp in schedule:
            for ev in emp:
                sweep[ev.start] += 1
                sweep[ev.end] -= 1
        
        sweep = dict(sorted(sweep.items()))
        res = []
        prefix = 0
        temp = None
        for t, s in sweep.items():
            prefix += s
            if prefix == 0 and not temp:
                temp = t
            else:
                if temp and prefix != 0:
                    res.append(Interval(temp, t))
                    temp = None

        return res
