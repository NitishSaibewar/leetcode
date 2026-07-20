class Solution(object):
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x: x[1] - x[0])
        cost = 0
        n = len(costs) // 2
        for i in range(n):
            cost += costs[i][1]   # City B
        for i in range(n, len(costs)):
            cost += costs[i][0]   # City A
        return cost