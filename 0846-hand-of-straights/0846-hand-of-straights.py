class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        freq = Counter(hand)
        cards = sorted(list(freq.keys()))

        
        for c in cards:
            if freq[c] == 0:
                continue
            while freq[c]:
                for i in range(c, c + groupSize):
                    if i not in freq:
                        return False
                    freq[i] -= 1
                    if freq[i] < 0:
                        return False
            
        
        return True
                

        