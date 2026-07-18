class Solution(object):
    def pickGifts(self, gifts, k):
        heap = []
        for g in gifts:
            heapq.heappush(heap, -g)
        while k>0:
                n = -heapq.heappop(heap)
                heapq.heappush(heap,-int(math.sqrt(n)))
                k -= 1
        return -sum(heap)