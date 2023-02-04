'''https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/'''

class Solution:
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalsum = sum(nums)
        partsum = totalsum//k
        if partsum*k!=totalsum:
            return False
        else:
            n = len(nums)
            self.collected = [0 for i in range(n)]
            # @cache
            def recursion(bucketnum,currsum, index):
                # print(self.collected)
                # print(bucketnum, currsum, index)
                if bucketnum==k:
                    # print("case1")
                    return True
                elif currsum==partsum:
                    # print("case3")
                    return recursion(bucketnum+1,0,0)
                elif index>=n or currsum>partsum:
                    # print("case2")
                    return False
                elif (bucketnum,currsum, index, tuple(self.collected)) in d:
                    return d[(bucketnum,currsum, index, tuple(self.collected))]
                else:

                    #If already picked, skip the element
                    if self.collected[index]:
                        # print("case4.1")
                        return recursion(bucketnum, currsum, index+1)
                    else:
                        # print("case4.2")
                        self.collected[index] = 1
                        pick = recursion(bucketnum, currsum+nums[index], index+1)
                        self.collected[index] = 0
                        notpick = recursion(bucketnum, currsum, index+1)
                        d[(bucketnum,currsum, index, tuple(self.collected))] = pick or notpick
                        return pick or notpick
            d = {}
            return recursion(0,0,0)