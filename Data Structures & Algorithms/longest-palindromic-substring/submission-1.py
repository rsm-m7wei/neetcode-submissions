class Solution:
    #写一个函数来检测该点出发是不是回文串；
    def ispal(self,s,left,right):
        while left>0 and right <len(s)-1 and s[left-1] ==s[right+1]:
            left -=1
            right +=1
        return left, right, right-left+1

    def longestPalindrome(self, s: str) -> str:
        #回文会有奇数和偶数长度的情况，我们都需要检测，并且存入最大的长度和其对应的left，right的坐标
        maxlen =0
        left =0
        right =0
        for i in range(len(s)-1):
            # 检测奇数的情况
            left1,right1, maxlen1 = self.ispal(s, i,i)
            if maxlen1>maxlen:
                maxlen =maxlen1
                left =left1
                right =right1
                #检测偶数的情况！！！这里必须注意，要这一位和下一位相同才能进入
            if s[i] == s[i+1]:
                left2,right2, maxlen2 = self.ispal(s, i,i+1)
                if maxlen2>maxlen:
                    maxlen =maxlen2
                    left =left2
                    right =right2
        #最后返回对应的位置的圈出来的字符
        return s[left:right+1]
            
        