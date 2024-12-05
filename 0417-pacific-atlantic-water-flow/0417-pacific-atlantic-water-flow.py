class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        idea - 
            BFS from left buttom corner and right top corner 
            return all the cells that can reach them 
        """
        res = []
        rows = len(heights)
        cols = len(heights[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        pasafic = set()
        atlantic = set()
        def bfs(r, c, subset):
            subset.add((r, c))
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and heights[new_r][new_c] >= heights[r][c] and (new_r, new_c) not in subset:
                    bfs(new_r, new_c, subset)
            return
                
        # pasafic 
        for r in range(rows):
            bfs(r, 0, pasafic)
            bfs(r, cols-1, atlantic)
        
        for c in range(cols):
            bfs(0, c, pasafic)
            bfs(rows-1, c, atlantic)
        return list(pasafic & atlantic)


