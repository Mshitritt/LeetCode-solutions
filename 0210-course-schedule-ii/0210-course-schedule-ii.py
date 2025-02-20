class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        
        seen = set()  
        instack = set()
        res = []

        def dfs(node):
            if node in instack:   # has cycle:
                return False
            if node in seen:  # Already processed, no cycle
                return True
            
            instack.add(node)
            for adj in graph[node]:
                if not dfs(adj):
                    return False
            
            instack.remove(node)  # Remove from recursion stack after processing
            seen.add(node)  # Mark as fully processed
            res.append(node)
            return True

        for i in range(numCourses):
            if i not in seen:
                if not dfs(i):  # If a cycle is detected, return []
                    return []
            
        
        return res[::-1]




