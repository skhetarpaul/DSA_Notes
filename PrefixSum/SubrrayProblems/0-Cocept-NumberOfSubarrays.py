class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dsum = {}
        ans = 0
        cursum = 0
        for i in range(len(nums)):
            cursum+=nums[i]
            
            if cursum==goal:
                ans+=1
            if cursum-goal in dsum:
                ans+=dsum[cursum-goal]
            if cursum in dsum:
                dsum[cursum]+=1
            else:
                dsum[cursum] = 1

        return ans
