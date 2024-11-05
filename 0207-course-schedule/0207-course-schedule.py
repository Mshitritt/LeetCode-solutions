class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        countCourses = 0
        for src, des in prerequisites:
            if src == des:
                return False
            if src not in adj:
                countCourses += 1
                adj[src] = [des]
            else:
                adj[src].append(des)
            
            if des not in adj:
                countCourses += 1
                adj[des] = []

        b = {}
        f = {}
        visited = set()
        time = [0]

        def DFS(node):
            visited.add(node)
            time[0] += 1
            b[node] = time[0]
            for v in adj[node]:
                if v not in visited:
                    DFS(v)

            time[0] += 1
            f[node] = time[0]

        for node in adj:
            if node not in visited:
                DFS(node)
        circle = set()
        for src, des in prerequisites:
            if b[src] > b[des] and f[src] < f[des]:
                circle.add(src)
                circle.add(des)
            
        for i in range(numCourses):
            if i in circle:
                return False

        
        
        return True




                


