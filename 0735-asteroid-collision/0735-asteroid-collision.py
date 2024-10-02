class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:  # While there's a potential collision (right-moving and left-moving)
                if stack[-1] < -ast:  # The top asteroid in the stack is smaller, so it explodes
                    stack.pop()
                    continue  # Check again if there's a new top to collide with
                elif stack[-1] == -ast:  # Both asteroids are the same size, both explode
                    stack.pop()  # Remove the top asteroid
                    break  # No more collisions to resolve, move to the next asteroid
                else:
                    break  # Current asteroid is smaller, it explodes and no changes to the stack
        
            else:
                stack.append(ast)  # Either no collision or the left-moving asteroid survived
        
        return stack

                

            
