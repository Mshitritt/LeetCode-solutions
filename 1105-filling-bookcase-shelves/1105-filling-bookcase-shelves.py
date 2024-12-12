class Solution:
    
        """
        for each book there have 2 options:
            1. start a new shelf
            2. added to cuurent shelf 
            return the minimum high of each option 
        """
        """
        def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
            # Cache to store previous computations
            memo = [[0 for _ in range(shelfWidth + 1)] for _ in range(len(books))]
            return self._dpHelper(books, shelfWidth, memo, 0, shelfWidth, 0)

        def _dpHelper(
            self, books, shelf_width, memo, i, remaining_shelf_width, max_height
        ):
            if i == len(books):
                return max_height
            if memo[i][remaining_shelf_width] != 0:
                return memo[i][remaining_shelf_width]
            else:
                current_book = books[i]
                # Calculate height of the bookcase if we put the current book on the new shelf
                option_1_height = max_height + self._dpHelper(
                    books,
                    shelf_width,
                    memo,
                    i + 1,
                    shelf_width - current_book[0],
                    current_book[1],
                )
                option_2_height = float("inf")
                if remaining_shelf_width >= current_book[0]:
                    # Calculate height of the bookcase if we put the current book on the current shelf
                    max_height_updated = max(max_height, current_book[1])
                    option_2_height = self._dpHelper(
                        books,
                        shelf_width,
                        memo,
                        i + 1,
                        remaining_shelf_width - current_book[0],
                        max_height_updated,
                    )

                # Store the smaller result in cache
                memo[i][remaining_shelf_width] = min(
                    option_1_height, option_2_height
                )
                return memo[i][remaining_shelf_width]
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
