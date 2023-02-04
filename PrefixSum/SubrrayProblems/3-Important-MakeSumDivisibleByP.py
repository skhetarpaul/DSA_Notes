'''Note that here we will be talking mostly about the subarrays and its sum hence prefix sum could be one of finest approaches to apply here.'''
'''Taking an example: Say we are given total Array sum==100 and p==7, that is from a given array we need to remove  a subarray suh that the remaining sum of the array is divisible by 6.

Fact is, we need sum of remaining array as 6*x. But we have 6*x + 4 i.e. 4 is remainder

So if somehow if we could remove a subarray that has 4 remaining, we will have the rest of sum as 6*x.

Illustration: totalsum = 100
we need remaining sum as 6*x

If we find somethijg currsum%p==remainder, that could be one case.
2nd case:
Part 1: currsum = 6*x + y
We previously have 6*x + z then if y-z==remainder, then also we can have the necessary condition fulfilled.

Part 2: Note line 33, here we did %p once more to cover negative cases as well:

Take instance of examples: [3,1,4,2] and p=6'''
class Solution:
    def minSubarray(self, nums, p: int) -> int:
        totalsum = sum(nums)
        n = len(nums)
        if totalsum%p==0:
            return 0
        else:
            remainder = totalsum%p
            currsum = 0
            minLen = n
            dcurr = {}
            #subarray sum must be of form p*x + remainder
            for i in range(n):
                currsum+=nums[i]
                if currsum%p==remainder or (currsum-remainder)%p==0:
                    minLen = min(minLen, i+1)
                if (currsum%p-remainder)%p in dcurr:
                    minLen = min(minLen, i-dcurr[(currsum%p-remainder)%p])
                dcurr[currsum%p] = i
            return minLen if minLen<n else -1
                