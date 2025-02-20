class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
        
        seen = set()
        instack = set()

        def dfs(i):
            if i in instack:
                return False    # detect cycle
            if i in seen:       # the node is processed
                return True

            instack.add(i)
            for adj in graph[i]:
                if not dfs(adj):
                    return False
                
            instack.remove(i)
            seen.add(i)
            return True




        for i in range(numCourses):
            if i not in seen and not dfs(i):
                return False
            
        return True
                    