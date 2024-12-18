class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)

        # prefix running time
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i-1] + runningCosts[i-1]
        
        def robotsValid(k):
            # return True if we can reach to cost < budget with k robots
            q = deque()
            i = 0
            
            # first window 
            while i < k:
                curr = chargeTimes[i]
                while q and chargeTimes[q[-1]] < curr:
                    q.pop()
                q.append(i)
                i += 1

            running = prefix[k] - prefix[0]
            mxVal = chargeTimes[q[0]]
            cost = mxVal + (k * running)

            if cost <= budget:
                return True

            # sliding window
            for i in range(k, n):
                # remove old number
                while q and q[0] < i-k:
                    q.popleft()
                
                # update freq
                curr = chargeTimes[i]
                while q and chargeTimes[q[-1]] < curr:
                    q.pop()
                q.append(i)
                mxVal = chargeTimes[q[0]]
                
                # calculate cost of window
                running = prefix[i] - prefix[i-k]
                cost = mxVal + (k * running)
                if cost <= budget:
                    return True
            return cost <= budget
        
        # Binary Search
        l = 1
        r = n

        while l <= r:
            k = (l+r)//2
            if robotsValid(k):
                l = k+1
            else:
                r = k-1
        return r
            

        
        
        

        

