class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #每一个格子能到达的方法等于左边和上面的格子相加
        #而第一行和第一列的方法都只有1，所以我们初始化为1
        #为了方便我们M*n都初始化为1，这样子我们后来的除了第一行第一列的地方都会变化的
        #但是首先我们排除最基本的情况 1*1
        if m == n == 1:
            return 1
        dp =[[1]*m for i in range(n)]
        for row in range(1,len(dp)):
            for col in range(1,len(dp[row])):
                dp[row][col] =dp[row][col-1]+dp[row-1][col]
        return dp[-1][-1]
