# https://leetcode.com/problems/prime-subtraction-operation/description/

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def findLesserElement(arr, target):
            low = 0
            high = len(arr)-1
            while high-low>1:
                mid = (low + high)//2
                if arr[mid]>=target:
                    high = mid-1
                else:
                    low = mid
            if arr[high]<target:
                return arr[high]
            elif arr[low]<target:
                return arr[low]
            return -1
        primes = []
        isPrime = [True for i in range(1001)]
        isPrime[0], isPrime[1] = False, False
        p = 2
        while p*p<=1000:
            if isPrime[p]:
                for x in range(p*p, 1001, p):
                    isPrime[x] = False
            p+=1
        for i, x in enumerate(isPrime):
            if x==True:
                primes.append(i)
        # print(primes)
        prev = 0
        for i, x in enumerate(nums):
            target = x-prev
            foundele = findLesserElement(primes, target)
            print(foundele, "for index: ", i, x)
            if foundele==-1:
                if i==0 or nums[i-1]<nums[i]:
                    prev = nums[i]
                    continue
                else:
                    return False
            else:
                nums[i], prev = nums[i]-foundele, nums[i]-foundele

        return True
        