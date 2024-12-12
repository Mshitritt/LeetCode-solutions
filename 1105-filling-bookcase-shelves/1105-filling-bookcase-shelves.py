class Solution:
    
        """
        for each book there have 2 options:
            1. start a new shelf
            2. added to cuurent shelf 
            return the minimum high of each option 
        """
        
       
        def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
            memo = {}

            def rec(i):
                if i >= len(books):
                    return 0 
                if i in memo:  
                    return memo[i]

                mxhight = 0
                remainWidht = shelfWidth
                res = float('inf')

                for j in range(i, len(books)): 
                    if remainWidht < books[j][0]:
                        break  
                    mxhight = max(mxhight, books[j][1])
                    remainWidht -= books[j][0]
                    res = min(res, mxhight + rec(j + 1))
                
                memo[i] = res
                return res

            return rec(0)
