class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        res = -1      
        rows = len(maze)  
        cols = len(maze[0])
        
        re = entrance[0]
        ce = entrance[1]
        distance = {}
        distance = {(re, ce): 0}
                
        q = deque()
        q.append([re, ce])
        while q:
            curr = q.popleft()
            r = curr[0]
            c = curr[1]
            if r+1 < rows and maze[r+1][c] == "." and (r+1, c) not in distance:
                distance[(r+1, c)] = distance[(r, c)]+1
                if r+1 == rows-1 or c == 0 or c == cols-1:
                    return distance[(r+1, c)]
                else:
                    q.append([r+1, c])

            if r-1 >= 0 and maze[r-1][c] == "." and (r-1, c) not in distance:
                distance[(r-1, c)] = distance[(r, c)]+1
                if r-1 == 0 or c == 0 or c == cols-1:
                    return distance[(r-1, c)]
                else:
                    q.append([r-1, c])

            if c+1 < cols and maze[r][c+1] == "." and (r, c+1) not in distance:
                distance[(r, c+1)] = distance[(r, c)]+1
                if c+1 == cols-1 or r == 0 or r == rows-1:
                    return distance[(r, c+1)]
                else:
                    q.append([r, c+1])

            if c-1 >= 0 and maze[r][c-1] == "." and (r, c-1) not in distance:
                distance[(r, c-1)] = distance[(r, c)]+1
                if c-1 == 0 or r == 0 or r == rows-1:
                    return distance[(r, c-1)]
                else:
                    q.append([r, c-1])
        return -1

                


            