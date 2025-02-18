class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(node, target, visited, parent):
            """Returns True if a path exists from node to target (cycle detection)."""
            if node == target:
                return True  # Cycle detected
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor == parent:  # Skip the parent node (to prevent false cycles)
                    continue
                if neighbor not in visited and dfs(neighbor, target, visited, node):
                    return True  # Found a cycle
            
            return False

        # Process edges one by one and check for cycles
        for u, v in edges:
            visited = set()
            if u in graph and v in graph and dfs(u, v, visited, -1):
                return [u, v]  # This edge creates a cycle
            
            # Add edge to graph (only if no cycle was found)
            graph[u].append(v)
            graph[v].append(u)

        return []




