class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        count = 1
        curr = word[0]
        for i in range(1, len(word)):
            if word[i] == curr:
                count += 1
                if count == 1:
                    curr = word[i]
                if count == 9:
                    res.append('9')
                    res.append(curr)
                    count = 0
            
            if word[i] != curr and count > 0:
                res.append(str(count))
                res.append(curr)
                curr = word[i]
                count = 1
            elif word[i] != curr:
                curr = word[i]
                count = 1
        
        res.append(str(count))
        res.append(curr)

        return "".join(res) 