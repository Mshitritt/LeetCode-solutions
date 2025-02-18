class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Graph building 
        graph = defaultdict(list)
        for s, e in edges:
            graph[s-1].append(e-1)
            graph[e-1].append(s-1)
        
        # Dfs function 
        seen = set()
        self.start = -1 # numbers stored LOCALLY ! 
        parents = [-1]*len(edges)
       
        def dfs(node):
            seen.add(node)
            for adj in graph[node]:
                if adj not in seen:
                    parents[adj] = node
                    dfs(adj)
                elif adj != parents[node]:
                    self.start = adj
                    parents[adj] = node

        for node in graph.keys():
            if node not in seen:
                dfs(node)

        
        # collect cycle's nodes
        cycle = set()
        node = self.start
        while True:
            cycle.add(node)
            node = parents[node]
            if node == self.start:
                break

        # find the last edge
        for s, e in edges[::-1]:
            if s-1 in cycle and e-1 in cycle:
                return [s,e]





