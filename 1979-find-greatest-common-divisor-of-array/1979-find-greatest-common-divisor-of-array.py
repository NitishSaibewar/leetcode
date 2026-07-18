class Solution(object):
    def findGCD(self, nums):
        a= min(nums)
        b=max(nums)
        while (b != 0):
            r = a % b
            a = b
            b = r
        return a
        