class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        n = len(rooms)
        visited = set([0])
   
        while q:
            room = q.popleft()
            for num in rooms[room]:
                if num not in visited:
                    visited.add(num)
                    q.append(num)
                if len(visited) == n:
                    return True
        return True if len(visited) == n else False
        

