#Extreme Bruteforce
class Solution:
    def canPartitionKSubsets(self, nums, k):
        totalsum = sum(nums)
        partitionsum = totalsum//k
        #If totalsum cannot be divided into k equal segments, break out and return False
        if partitionsum*k!=totalsum:
            return False
        else:
            bucket = [partitionsum for i in range(k)]
            n = len(nums)
            def recursion(index, bucket):
                if index==n:
                    return True if bucket==[0]*k else False
                else:
                    isPossible = False

                    for ki in range(k):
                        if nums[index]<=bucket[ki]:
                            print(bucket[:ki], [bucket[ki]-nums[index]], bucket[ki+1:] )
                            print(bucket[:ki] + [bucket[ki]-nums[index]] + bucket[ki+1:])
                            possible = recursion(index+1, bucket[:ki] + [bucket[ki]-nums[index]] + bucket[ki+1:])
                            isPossible = possible + isPossible
                    return isPossible
            return recursion(0,bucket)

# =============================================================================

#Brute force: Recursio with DFS
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
                elif (bucketnum,currsum, index) in d:
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

            
        
                
            
        