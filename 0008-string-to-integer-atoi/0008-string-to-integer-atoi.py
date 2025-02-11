class Solution:
    def myAtoi(self, s: str) -> int:
        pos = True
        num = 0
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and s[i] in "-+":
            if s[i] == "-":
                pos = False
            i += 1
        
        if i < len(s):
            for l in s[i:]:
                if l in "-+" or not l.isdigit():
                    return num
                
                num *= 10
                if pos:
                    num += int(l)
                else:
                    num -= int(l)
                
                
        if num > 0 and 2**31 - 1 <= num:
            return 2**31 - 1
        if num < 0 and num <= -2**31:
            return -2**31
                    
                    
        return num