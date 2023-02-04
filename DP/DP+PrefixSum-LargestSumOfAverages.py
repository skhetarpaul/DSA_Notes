class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefixsum = [i for i in nums]
        for i in range(1, len(nums)):
            prefixsum[i]+=prefixsum[i-1]
        def getPrefixSum(start, end):
            
            ans = 0
            if start>0:
                ans = prefixsum[end]-prefixsum[start-1]
            else:
                ans =  prefixsum[end]
            ans/=(end-start+1)
            # print("start {} and end {} ans {}".format(start, end, ans))
            return ans
        @cache
        def recursion(index, start, parts):
            if index==len(nums):
                if start<len(nums):
                    return getPrefixSum(start, index-1)
                else:
                    return float("-inf")

            else:
                #continue the array, dont end array here
                continued = recursion(index+1, start, parts)
                #end array here
                stopped = float("-inf")
                if parts<k-1:
                    stopped = getPrefixSum(start, index) + recursion(index+1, index+1, parts+1)
                return max(continued, stopped)
        return recursion(0, 0, 0)