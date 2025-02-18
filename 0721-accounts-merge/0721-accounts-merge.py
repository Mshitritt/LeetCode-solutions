class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        mail_to_name = defaultdict(list)

        # build graph 
        for acc in accounts:
            n = len(acc)
            name = acc[0]
            if n == 2:
                mail = acc[1]
                mail_to_name[mail] = name
                graph[mail] = [mail]
            else:
                for i in range(2, n):
                    prev, cur = acc[i-1], acc[i]
                    mail_to_name[prev] = name
                    mail_to_name[cur] = name
                    graph[prev].append(cur)
                    graph[cur].append(prev)
        
        # dfs function 
        def dfs(mail):
            for adj in graph[mail]:
                if adj not in seen:
                    seen.add(adj)
                    dfs(adj)
        
        # build results 
        res = []
        visited = set() # total mail we have descovered
        
        for mail in graph.keys():
            seen = set()    # total mails of same person
            if mail not in visited:
                visited.add(mail)
                dfs(mail)
                name = mail_to_name[mail]
                mails = []
                visited.update(seen)
                while seen:
                    mails.append(seen.pop())
                mails.sort()
                mails.insert(0, name)
                res.append(mails)
        return res





            
            
            

            
            
            



