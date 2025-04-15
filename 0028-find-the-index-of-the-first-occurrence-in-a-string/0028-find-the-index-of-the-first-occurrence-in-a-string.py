class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       
        if not needle:
            return 0
        
        lps = [0] * len(needle)
        length = 0  # length of the previous longest prefix suffix

        i = 1  # start from second char
        while i < len(needle):
            cuur_i, curr_l = needle[i], needle[length]
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]  # backtrack
                else:
                    lps[i] = 0
                    i += 1
        i = 0 # haystack
        j = 0 # needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == len(needle):
                return i - len(needle)
        return -1

                    

            
