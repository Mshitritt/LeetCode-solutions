class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        freq = Counter(hand)
        cards = sorted(list(freq.keys()))

        groups = 0
        for c in cards:
            if c not in freq:
                continue
            for i in range(c, c + groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1
                if not freq[i]:
                    del freq[i]
            groups += 1
        
        return True
                

        