import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        heap = []
        for i in range(len(nums1)):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))
        res = []
        while k > 0:
            sum , row , col = heapq.heappop(heap)
            res.append([nums1[row],nums2[col]])
            if col + 1 < len(nums2):
                heapq.heappush(heap,(nums1[row] + nums2[col + 1],row, col+1))
            k -= 1
        return res