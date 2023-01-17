
# https://leetcode.com/problems/gas-station/description/
# An algoritm like Kadanse's algorithm

class Solution:
    
    def canCompleteCircuit(self, gas, cost):
        #base case
        if sum(gas)-sum(cost)<0:
            return -1
        n = len(cost)
        total, curr_sum = 0,0
        start = 0
        for i in range(n):
            total+=gas[i]-cost[i]
            curr_sum+=gas[i]-cost[i]
            if curr_sum<0:
                start=  i+1
                curr_sum = 0
        return start