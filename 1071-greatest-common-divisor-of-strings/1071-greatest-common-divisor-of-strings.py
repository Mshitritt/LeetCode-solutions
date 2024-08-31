class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # find the shortest word
        short_w = str1
        long_w = str2
        ls = len(str1)
        ll = len(str2)
        if ll < ls:
            short_w = str2
            long_w = str1
            ls, ll = ll, ls

        # find t dividor
        t = short_w[:ls]
        while t:
            # return true if exist item that not equal to ''
            srt_lst = short_w.split(t)
            lng_lst = long_w.split(t)
            exists_short = any(item != '' for item in srt_lst)
            exists_long = any(item != '' for item in lng_lst)

            if exists_short is False and exists_long is False:
                return t
            else:
                ls -= 1
                t = short_w[:ls]

        return ''


        

