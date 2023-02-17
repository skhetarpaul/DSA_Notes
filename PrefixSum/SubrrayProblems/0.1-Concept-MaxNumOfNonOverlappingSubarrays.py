# https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

'''AN important question, this requires us to find the maximum number of non overlapping subarrays which can be formed by summation of target.

Further using Greedy Job scheduling to maximize output.
Give following is a Brute force approach'''

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dsums = {}
        cursum = 0
        dset = set()
        for i in range(len(nums)):
            cursum+=nums[i]
            
            if cursum in dsums:
                dsums[cursum].append(i)
            else:
                dsums[cursum] = []
                dsums[cursum].append(i)
            if cursum==target:
                dset.add((0,i))
            if cursum-target in dsums:
                
                for item in dsums[cursum-target][-2:]:
                    if item+1<=i:
                        dset.add((item+1,i)) 
        # print(dset)
        if len(dset)==0:
            return 0
        dlist = sorted(list(dset), key = lambda x: x[1])
        print(dlist)
        count = 1
        prevend = dlist[0][1]
        for i in range(1, len(dlist)):
            if dlist[i][0]>prevend:
                prevend = dlist[i][1]
                count+=1
        return count


'''Following is the implementation of another better approach, Make the first subarray first and then think about the rest.
Another important point to look here is, we reset the dictionary as soon as we ind cursum-target in the dictionary, elsewise we will keep on appending the cursum to dictionary as we get along the items.'''

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dsums = {0: 1}
        cursum = 0
        ans = 0
        for i in range(len(nums)):
            cursum+=nums[i]
            if cursum-target in dsums:
                print(i, "at i")
                ans+=1
                dsums = {cursum: 1}
            else:
                dsums[cursum] = 1
                
        return ans