class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #首先，创建一个m+1，n+1的全是0的矩阵，这里的数字代表着能当前步骤的情况下子串的最大长度
        #横竖的第一个都是0之后才是这个text
        rows = len(text1)+1
        cols = len(text2)+1
        #创建矩阵,!!!队列中的队列
        #注意这里先是cols再是rows
        dp =[[ 0 for i in range(cols)]for j in range(rows)]
        for row in range(1,rows):
            for col in range(1,cols):
                # dp 的第一行和第一列表示：其中一个字符串为空时，
                #最长公共子序列长度为 0（LCS 的 base case）
                #所以这的dp的坐标-1才是text里面对应的坐标
                #text1 和 text2 是一维字符串，只能用 row-1 / col-1 单索引，
                #不能当成二维数组写成 [row-1][col-1]
                if text1[row-1]== text2[col-1]:
                    dp[row][col]=dp[row-1][col-1]+1
                # 字符不匹配，当前字符不能同时加入公共子序列，只能从上或左继承最大值
                else:
                    dp[row][col]=max(dp[row-1][col],dp[row][col-1])
        #for 循环结束后，循环变量不会消失，为“最后一次取到的值,所以这里就是右下角的那一个格子
        return dp[row][col]

