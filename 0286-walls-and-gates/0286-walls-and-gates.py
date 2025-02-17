class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    while q:
                        cur_r, cur_c = q.pop()
                        for dr, dc in directions:
                            nxt_r, nxt_c = cur_r + dr, cur_c + dc
                            if 0 <= nxt_r < rows and 0 <= nxt_c < cols:
                                if rooms[cur_r][cur_c]+1 < rooms[nxt_r][nxt_c]:
                                    rooms[nxt_r][nxt_c] = rooms[cur_r][cur_c]+1
                                    q.append([nxt_r, nxt_c])
                                    
            

