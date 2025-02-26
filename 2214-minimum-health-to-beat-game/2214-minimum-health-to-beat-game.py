class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        if not armor:
            return sum(damage) + 1
            
        health = 1
        maxDemage = 0

        for num in damage:
            health += num
            maxDemage = max(maxDemage, num)

        #return health - min(armor, maxDemage)
        return sum(damage) - min(armor, max(damage)) +1