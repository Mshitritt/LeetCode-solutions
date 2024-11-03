class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(set)
        for src, dest in connections:
            adj[src].add(dest)
            adj[dest].add(src)
            
        # calculate distances from 0
        distance = {0:0}
        q = deque()
        q.append(0)
        while q:
            curr = q.popleft()
            for a in adj[curr]:
                if a not in distance:
                    distance[a] = distance[curr]+1
                    q.append(a)
            

        roads = 0
        for src, dest in connections:
            if distance[src] < distance[dest]:
                roads += 1
        return roads





            

        
        
            
            
        return roads
       
            


