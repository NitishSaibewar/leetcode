class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = []
        n= len(matrix)
        for i in range(n):
            heapq.heappush(heap,(matrix[i][0],i,0))
        while k > 1:
            val, row, col = heapq.heappop(heap)
            if col + 1 < n:
                heapq.heappush(heap,(matrix[row][col + 1], row, col+1))
            k -= 1
        return heapq.heappop(heap)[0]