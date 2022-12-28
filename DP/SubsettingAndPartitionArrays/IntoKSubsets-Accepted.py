class Solution:
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalsum = sum(nums)
        partsum = totalsum//k
        if partsum*k!=totalsum:
            # print("here")
            return False
        else:
            n = len(nums)
            self.collected = [0 for i in range(n)]
            # @cache
            def recursion(bucketnum,currsum, index):
                if bucketnum==k:
                    return True
                elif currsum==partsum:
                    return recursion(bucketnum+1,0,0)
                elif (bucketnum,currsum, index, tuple(self.collected)) in d:
                    return d[(bucketnum,currsum, index, tuple(self.collected))]
                else:
                    for j in range(index, n):
                        if self.collected[j]==1 or currsum + nums[j]>partsum:
                            continue
                        self.collected[j] = True
                        if recursion(bucketnum, currsum + nums[j], j+1):
                            d[(bucketnum,currsum, index, tuple(self.collected))] = True
                            return True
                        self.collected[j] = False
                    d[(bucketnum,currsum, index, tuple(self.collected))] = False
                    return False
            d = {}
            return recursion(0,0,0)

            
        