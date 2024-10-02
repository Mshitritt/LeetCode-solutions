class Solution:
    def decodeString(self, s: str) -> str:
        """
        Explanation 
        for c in s:
            if c is digit --> accomulate digits 
            if c is '['   --> add num and curr_str into stack 
            if c is ']'   --> pop string from stack and add to res_str many times as last number
            if c is letter -> accomulate into curr_str
        """
        stack = []
        num = ""

        curr_str = ""

        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(int(num))
                stack.append(curr_str)
                num = ""
                curr_str = ""
            elif c.islower():
                curr_str += c
            else:
                # c = ']'
                temp_str = stack.pop()
                temp_num = stack.pop()
                curr_str = temp_str + curr_str * temp_num

        return curr_str

            

