'''My intuition to use Binary Search here:
    Note that we are asked to optimize i.e. either Minimize or maximize the cost, that is definitely a terminating condition.
    Also, we dont have a specific value the minimum capacity required can be anything from 1 to sum(weights).
    So why not we do a Binary search considering a fact, if a capacit is not valid all capacities below that capacities will also be invalid.
    Similarly, if a capacity is valid then all capacities above it would be valid and to find minimum we need to scroll to lesser values of capacity.'''
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        maxw = sum(weights)
        minw = 1
        n = len(weights)
        maxi = max(weights)
        # self.ans = 0
        while minw<=maxw:
            mid = (minw + maxw)//2
            if mid<maxi:
                minw = mid+1
            else:
                daysreqd = 1
                curwt = weights[0]
                for i in range(1,n):
                    if curwt + weights[i]<=mid:
                        curwt = curwt + weights[i]
                    else:
                        daysreqd+=1
                        curwt = weights[i]
                if daysreqd<=days:
                    # self.ans = mid
                    maxw = mid-1
                else:
                    minw = mid+1
        return minw