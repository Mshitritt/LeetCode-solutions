class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Graph building 
        graph = defaultdict(list)
        for s, e in edges:
            graph[s-1].append(e-1)
            graph[e-1].append(s-1)
        
        # Dfs function 
        self.seen = set()
        self.start = -1
        self.parents = [-1]*len(edges)
        seenVAL = self.seen
        startVAL = self.start
        parentsArray = self.parents
       
        def dfs(node):
            self.seen.add(node)
            for adj in graph[node]:
                if adj not in self.seen:
                    self.parents[adj] = node
                    dfs(adj)
                elif adj != self.parents[node] and self.start == -1:
                    self.start = adj
                    self.parents[adj] = node

        for node in graph.keys():
            if node not in self.seen:
                dfs(node)

        
        # collect cycle's nodes
        cycle = set()
        node = self.start
        while True:
            cycle.add(node)
            node = self.parents[node]
            if node == self.start:
                break
            


        
        # find the last edge
        for s, e in edges[::-1]:
            if s-1 in cycle and e-1 in cycle:
                return [s,e]





