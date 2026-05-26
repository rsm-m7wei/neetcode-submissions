class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
       #应为我们需要高频的从list里面找元素，所以转化成set速度能上升很多
        wordDict = set(wordDict)
        #接下来，我们要创建一个长度是s+1的全是false的队列，这样在切片的时候[]方便
        n = len(s)+1
        dp = [False]*n
        #我们初始化第0号，代表没有字符的时候一定是True
        dp[0]= True
        #接下来，为了提高效率，我们可以创建一个list来存放true的位置，以后我们就从这里面到i来查看分段来提高效率
        trues =[0]
        #从第一位开始，正好第一个字母就对应1，而不是0
        #!!!这里的1到n中间是，不是：
        for i in range(1,n):
            for j in trues:
                if s[j:i] in wordDict:
                    dp[i]=True
                    trues.append(i)
                    break
        return dp[-1]