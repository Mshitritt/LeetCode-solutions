class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = sorted(zip(positions, healths, directions, range(n)))
        stack = []
        survivors = []

        for pos, health, direction, index in robots:
            if direction == 'R':
                stack.append((health, index))
            else:  # direction == 'L'
                while stack and health > 0:
                    right_health, right_index = stack.pop()
                    if right_health > health:
                        stack.append((right_health - 1, right_index))
                        health = 0
                    elif right_health < health:
                        health -= 1
                    else:  # right_health == health
                        health = 0
                
                if health > 0:
                    survivors.append((health, index))

        # Add remaining robots from the stack (robots moving right that never collided)
        survivors.extend(stack)

        # Sort survivors by their original indices
        survivors.sort(key=lambda x: x[1])
        return [health for health, _ in survivors]
                    
        
        
        


            
