class Solution(object):
    def minStoneSum(self, piles, k):
        heap = []
        for p in piles :
            heapq.heappush(heap, -p)
        while k > 0:
            n = -heapq.heappop(heap)
            heapq.heappush(heap, -(n -(n//2)))
            k -= 1
        return -sum(heap)
