# Very Important question: Covers following concepts:
# Circular subarray
# Minimum sum through Kadanes algorithm
# Kadanes algorithm
# Prefix and suffix sum

class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        def Kadanes(nums):
            currsum = 0
            maxsum = float("-inf")
            for i in range(len(nums)):
                currsum+=nums[i]
                maxsum = max(currsum, maxsum)
                if currsum<0:
                    currsum = 0
            return maxsum

        if len(nums)==1:
            return nums[0]
        else:
            #To calculate 2 Kadane sum, one is for cirular array that basically consists of prefix and suffix sum excluding a minsum.
            temparr = [-1*nums[i] for i in range(len(nums))]
            temptotalsum = sum(temparr)
            minSum = Kadanes(temparr)
            if minSum==temptotalsum:
                #This boundary case covers, if all numbers are negative in array
                return Kadanes(nums)
            else:
                normalsum = Kadanes(nums)
                specialsum = -1*temptotalsum-(-1*minSum)
                return max(specialsum, normalsum)
