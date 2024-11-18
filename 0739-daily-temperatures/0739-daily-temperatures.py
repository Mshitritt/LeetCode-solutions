class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        stack = []
        res = [0]*len(temperatures) #(temp, index)
        for i , t in enumerate(temp):
            while stack and stack[-1][0] < t:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
                
            
    
            
            stack.append([t, i])
            

        return res
                