class SmallestInfiniteSet:

    def __init__(self):
        dt = []
        for i in range(1, 1001):
            dt.append(i)
        heapq.heapify(dt)
        self.heap = dt

    def popSmallest(self) -> int:
        return heapq.heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)
        return None
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)