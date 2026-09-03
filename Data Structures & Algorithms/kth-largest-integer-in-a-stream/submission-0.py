class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heaplist = nums
        self.k = k
        heapq.heapify(self.heaplist)
        while len(self.heaplist) > self.k:
            heapq.heappop(self.heaplist)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heaplist, val)

        if len(self.heaplist) > self.k:
            heapq.heappop(self.heaplist)
        return self.heaplist[0]
        
