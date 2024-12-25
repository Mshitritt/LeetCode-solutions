class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0]*len(speed)
        for i in range(len(speed)):
            pos = position[i]
            t = (target - pos) / speed[i]
            time[i] = (pos, t)

        time.sort()
        res = 1
        for i in range(1, len(time)):
            if time[i][1] < time[i-1][1]:
                res += 1
        return res

