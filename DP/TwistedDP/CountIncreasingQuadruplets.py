'''https://leetcode.com/problems/count-increasing-quadruplets/description/
https://www.youtube.com/watch?v=RxsbwiXvNkQ
Note the optimized version carefully, as to know how the problem of DP can be broken down into subproblem and solve each to get the fins;l answer.

Important concept for nested loops": Optiized code- Line no. 51- 58'''

# Brute force approach


class Solution:
    def countQuadruplets(self, nums) -> int:
        # @cache
        d = {}
        def recursion(index, arr):
            if len(arr)==4:
                return 1
            elif index==len(nums):
                return 0
            elif (index, tuple(arr)) in d:
                return d[(index, tuple(arr))]
            else:
                #donot pick the cuurrent element
                casei = recursion(index+1, arr)
                caseii = 0
                if arr==[] or (len(arr)!=2 and nums[index]>arr[-1]):
                    caseii = recursion(index+1, arr + [nums[index]])
                elif len(arr)==2 and nums[index]>arr[0] and nums[index]<arr[-1]:
                    caseii = recursion(index+1, [arr[0], nums[index], arr[-1]])
                d[(index, tuple(arr))] = casei + caseii
                return casei + caseii
        return recursion(0, [])
                    


#Optimized version:
class Solution:
    def countQuadruplets(self, nums) -> int:
        n = len(nums)
        greaterThan = [[0 for i in range(len(nums))] for i in range(len(nums))]
        lessThan = [[0 for i in range(len(nums))] for j in range(len(nums))]
        #greaterThan: No of elements from i to j where nums[i]<nums[j]
        for i in range(n):
            greater = 0
            for j in range(i+1, n):
                if nums[j]>nums[i]:
                    greater+=1
                greaterThan[i][j] = greater
        
        #lessThan[i,j]: No of elements in range(i,j] lesser than j

        for i in range(n):
            smaller = 0
            for j in range(i-1, -1,-1):
                if nums[i]>nums[j]:
                    smaller+=1
                lessThan[j][i] = smaller
        res = 0
        for j in range(1, n-2):
            for k in range(j+1, n-1):
                if nums[j]>nums[k]:
                    possible_i = lessThan[0][k]- lessThan[j][k]
                    possible_l = greaterThan[j][n-1]-greaterThan[j][k]
                    res+=possible_i*possible_l
        return res
