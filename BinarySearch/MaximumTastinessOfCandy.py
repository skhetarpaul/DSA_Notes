# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description/
'''
Hints to solve similar questions:
    1. Maximize the minimu,
    2. We are assuming a value and try for every possible value from minrange to maxrange.
    We dont know wht could be the answer, this method will be a good approach to solve problems relating to try every possible value in the given range
    Here range was 0, 1000000000

    3.Sorting makes no effect
'''



class Solution:
    def maximumTastiness(self, price, k):
        prices = sorted(price)
        n = len(prices)
        self.ans = 0
        def binarySearch(low, high):
            if low<=high:
                mid = (low+high)//2
                last = 0
                cnt = 1
                for i in range(1, n):
                    if prices[i]-prices[last]>=mid:
                        cnt+=1
                        last = i
                if cnt>=k:
                    # print("count: {} low: {} high: {}".format(cnt, low, high))
                    self.ans = mid
                    binarySearch(mid+1, high)
                else:
                    # print("count: {} low: {} high: {} did not comply".format(cnt, low, high))
                    binarySearch(low, mid-1)
            
            return self.ans
        return binarySearch(0, 10**9)