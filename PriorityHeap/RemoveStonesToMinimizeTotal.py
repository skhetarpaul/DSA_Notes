#HINT: Whenever multiple times sorting is reqd. , you might need  priority Queue to solve question.
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/
import heapq

class Solution:
    def minStoneSum(self, piles, k):
        sortedp = []
        for p in piles:
            heapq.heappush(sortedp,(-1)*p)

        while k!=0:
            k-=1
            item = (-1)*heapq.heappop(sortedp)
            heapq.heappush(sortedp, (-1)*(item-item//2))
            # print(sortedp)
        return (-1)*sum(sortedp)

        