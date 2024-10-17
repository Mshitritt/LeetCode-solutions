class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        comb = []

        def helper(temp: str, open_counter, close_counter):
            if close_counter == n:
                comb.append(temp)
            elif open_counter == n and close_counter < n:
                helper(temp + ")", open_counter, close_counter+1)

            else:
                # open_counter, close_counter < n
                if open_counter > close_counter:
                    # we can add open or close parentheses

                    helper(temp + "(", open_counter + 1, close_counter)
                    helper(temp + ")", open_counter, close_counter + 1)
                else:

                    return helper(temp + "(", open_counter+1, close_counter)

        helper("(", 1, 0)
        return comb

         
