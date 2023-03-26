#User function Template for python3
'''This is the first exampl of PartitionDP: Matrix Chain mULTIPLIcation

Partition DP steps involve:
1. Start witht he entire partion (i,j)
2. Break into smaller partion of (i, k) and maybe (k+1, j)-> Try all partitions
3. return the best 2 partitions'''

'''Whenever you are asked to do a problem-> solve a problem in a particular pattern-> Partition DP applies'''
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        dp = {}
        def recursion(i,j):
            if i==j:
                return 0
            elif (i,j) in dp:
                return dp[(i,j)]
            else:
                mini = float("inf")
                for k in range(i, j):
                    steps = recursion(i, k) + recursion(k+1, j) + arr[i-1]*arr[k]*arr[j]
                    mini = min(mini, steps)
                dp[(i,j)] = mini
                return mini
        # return recursion(1, N-1)
        
        def Tabulation():
            dp = [[0 for i in range(N+1)] for j in range(N+1)]
            for i in range(N-1, -1,-1):
                for j in range(i, N):
                    if i==j:
                        dp[i][j] = 0
                    else:
                        mini = float("inf")
                        for k in range(i, j):
                            steps = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                            mini = min(steps, mini)
                        dp[i][j] = mini
            return dp[1][N-1]
                    
        return Tabulation()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends