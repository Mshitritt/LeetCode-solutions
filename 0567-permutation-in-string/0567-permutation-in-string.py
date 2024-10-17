class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        # Initialize frequency counts for s1 and the first window in s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # TRY TO SOLVE WITH FIX SIZE OF WINDOW
        for i in range(1, len(s2) - len(s1)+1):
            if s1Count == s2Count:
                return True
            else:
                s2Count[ord(s2[i - 1]) - ord('a')] -= 1
                s2Count[ord(s2[i+len(s1)-1]) - ord('a')] += 1

        return s1Count == s2Count




                


                