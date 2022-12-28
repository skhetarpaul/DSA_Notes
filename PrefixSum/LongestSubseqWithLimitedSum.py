#A questio utilizing knowledge of P

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        prefixSum = [0]*n
        for i in range(len(nums)):
            if i>0:
                prefixSum[i] = prefixSum[i-1] + nums[i]
            else:
                prefixSum[i] = nums[i]
        def findLesserOrEquivalent(target, arr):
            low = 0
            high = len(arr)-1
            while high-low>1:
                mid = (low + high)//2
                if arr[mid]>target:
                    high = mid-1
                else:
                    low = mid
            if arr[high]<=target:
                return high
            elif arr[low]<=target:
                return low
            else:
                return -1
        ans = [0 for i in range(len(queries))]
        for i in range(len(queries)):
            q = queries[i]
            #find an element in prefix sum, just equal or lesser
            pindex = findLesserOrEquivalent(q, prefixSum)
            if pindex==-1:
                ans[i] = 0
            else:
                ans[i] = pindex+1
        return ans

