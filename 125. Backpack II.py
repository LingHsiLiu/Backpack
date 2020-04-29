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
