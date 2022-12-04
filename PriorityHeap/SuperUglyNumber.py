#Aother approach, DP for solving Ugly number and Super Ugly number.
'''
Make a dp array to store the nth smallest number made with these primes.
The number in primes, that helped making the nth Ugly number, increase its pointer to 1.
Next time, you will compare likewise,
'''
# https://leetcode.com/problems/super-ugly-number/submissions/854503970/

# This is a TLE Approach, check for better ones.

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pointers = [1 for i in range(len(primes))]
        dp = [0 for i in range(n+1)]
        dp[0], dp[1] =0,1
        for i in range(2, n+1):
            minima = float("inf")
            for x in range(len(primes)):
                minima = min(minima, primes[x]*dp[pointers[x]])
                # print(primes[x]*pointers[x])
            #I got the minima
            dp[i] = minima
            for x in range(len(pointers)):
                if minima==primes[x]*dp[pointers[x]]:
                    pointers[x]+=1
        # print(dp)
        return dp[n]
