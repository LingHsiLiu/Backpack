class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        dp = [[0 for j in range(m+1)] for i in range(len(A) + 1)]
        for i in range(len(A) + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif (A[i - 1] > j):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i -1][j - A[i - 1]] + V[i - 1])
        return dp[len(A)][m]

# Another method
#         f = [0 for i in xrange(m+1)]
#         print(f)
#         n = len(A)
#         for i in range(n):
#             for j in xrange(m, A[i]-1, -1):
#                 f[j] = max(f[j] , f[j-A[i]] + V[i])
#                 print(f)
#         return f[m]
