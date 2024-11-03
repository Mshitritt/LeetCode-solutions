class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c] == 1:
                    isConnected[r][c] = 0
                    res += 1
                    q = deque([r])
                    while q:
                        curr = q.popleft()
                        for c_idx in range(cols):
                            if isConnected[curr][c_idx] == 1:
                                isConnected[curr][c_idx] = 0
                                q.append(c_idx)

                        
        return res
