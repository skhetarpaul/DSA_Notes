import copy
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        n = len(nums)
        nums.sort()
        low = 0
        high = nums[n-1]-nums[0]
        def isValid(target, x):
            print(target)
            i = 1
            while i<n:
                if nums[i]-nums[i-1]<=target:
                    x-=1
                    i+=2
                else:
                    i+=1
            # for i in range(1, n):
            #     if nums[i]-nums[i-1]<=target:
            #         print(i, i-1, "forms valid pair")
            #         x-=1
            #         i+=1
            return x<=0

        while low<=high:
            mid = (low + high)//2
            if isValid(mid, copy.deepcopy(p)):
                print("mid = ", mid, p)
                high = mid-1
            else:
                low = mid+1
        return low