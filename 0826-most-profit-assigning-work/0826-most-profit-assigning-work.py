class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        job = []
        for i in range(len(profit)):
            job.append([difficulty[i], profit[i]])
        job.sort()
        worker.sort()
        profit = 0
        best = 0
        j = 0
        for w in worker:
            while j < len(job) and job[j][0] <= w:
                best = max(best, job[j][1])
                j += 1
            profit += best
        return profit