class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        i = 0
        for src, dest in equations:
            temp1 = [dest, values[i]]
            temp2 = [src, 1/values[i]]
            adj[src].append(temp1)
            adj[dest].append(temp2)
            i += 1
        
        res = []
        idx = 0
        
        for a, b in queries:
            prod = {a: 1}
            if a not in adj or b not in adj:
                res.append(-1)
            elif a == b:
                res.append(1)
            else:
                q = deque()
                q.append(a)
                while q:
                    curr = q.popleft()
                    for nighbor in adj[curr]:
                        if nighbor[0] not in prod:
                            prod[nighbor[0]] = prod[curr]*nighbor[1]
                            q.append(nighbor[0])
                        
                if b not in prod:
                    res.append(-1)
                else:
                    res.append(prod[b])
        
        return res







