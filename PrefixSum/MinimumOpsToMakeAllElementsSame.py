# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/description/

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        def findEquivalentOrLesser(arr, target):
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
        n = len(nums)
        prefixsum = [0 for i in range(len(nums))]
        prefixsum[0] = nums[0]
        for i in range(1, n):
            prefixsum[i]+=prefixsum[i-1] + nums[i]
        prefixsum = [0] + prefixsum
        # print(prefixsum)
        ans = []
        for q in queries:
            curr = 0
            leindex = findEquivalentOrLesser(nums, q)
            # print(leindex, "value of leindex")
            curr+= q*(leindex+1) - prefixsum[leindex+1]
            curr+= prefixsum[n]-prefixsum[leindex+1]-q*(n-leindex-1)
            ans.append(curr)
        return ans
