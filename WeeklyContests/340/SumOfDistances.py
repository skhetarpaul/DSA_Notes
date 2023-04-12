# https://leetcode.com/problems/sum-of-distances/description/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        docc = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in docc:
                docc[nums[i]].append(i)
            else:
                docc[nums[i]] = [i]

        def findIndex(target, arr):
            low = 0
            high = len(arr)-1
            while low<=high:
                mid = (low + high)//2
                if arr[mid]==target:
                    return mid
                elif arr[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
            return -1

        def calculatePrefixSum(arr):
            k = len(arr)
            prsum = [0]*k
            prsum[0] = arr[0]
            for i in range(1, k):
                prsum[i]+=prsum[i-1] + arr[i]
            return prsum
        for key, val in docc.items():
            prsum = calculatePrefixSum(val)
            docc[key] = [val, prsum]
        # print(docc)

        ans = [0]*n
        for i in range(n):
            #find nums[i] in docc[nums[i]]
            reqdIndex = findIndex(i, docc[nums[i]][0])
            # print(reqdIndex, "required index")
            maxLen = len(docc[nums[i]][0])
            if maxLen==1:
                ans[i]=0
            else:
                # print(docc[nums[i]])
                ans[i] = docc[nums[i]][1][-1] - docc[nums[i]][1][reqdIndex] - (maxLen-1-reqdIndex)*i
                if reqdIndex>0:
                    ans[i] += reqdIndex*i - docc[nums[i]][1][reqdIndex-1]
        return ans


                