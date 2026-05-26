class Solution:
    def ispalin(self,s,left,right):
        #is in range and qualify question rule
        #right cna only be last 2 position because we need check i+1 and i are the same
        while  left>0 and right <len(s)-1 and s[left-1] ==s[right+1]:
            left-=1
            right+=1
        return left, right, right-left+1

    def longestPalindrome(self, s: str) -> str:
        #edge case
        if not s:
            return ''
        if len(s)==1:
            return s
        #we can not go the the last position 
        #set some globale variables
        left =0 
        right =0
        maxlen =0
        for i in range(len(s)):
            #we check if this alpha potion ca be a palinfrommic
            left1,right1,maxlen1 = self.ispalin(s,i,i)
            if maxlen1>maxlen:
                maxlen =maxlen1
                left =left1
                right =right1
            #if i and i+1 are the same,we have additional check
            # and 是从左往右边计算的
            if i+1<len(s) and s[i] ==s[i+1]  :
                left2,right2,maxlen2 = self.ispalin(s,i,i+1)
                if maxlen2>maxlen:
                    maxlen =maxlen2
                    left =left2
                    right =right2
        return s[left:right+1]




# class Solution:
# #写一个函数来检测该点出发是不是回文串；
# # def ispal(self,s,left,right):
# # while left>0 and right <len(s)-1 and s[left-1] ==s[right+1]:
# # left -=1
# # right +=1
# # return left, right, right-left+1

# #我们首先写一个函数来检查从这个位置出发最长的回文长度，我们需要检测是否是在有效区间，并符合规则
# def helper(self, s, left, right):
# #只能到倒数第二个位置来避免下面的函数检查的时候越界
# while left<=right and left>0 and right <len(s)-1 and s[left-1] ==s[right+1]:
# left -=1
# right+=1
# return left, right, right-left+1

# def longestPalindrome(self, s: str) -> str:
# #初始化我们需要的参数：
# maxlen =0 
# left = 0
# right = 0
# #不越界
# for i in range(len(s)-1):
# left1,right1,maxlen1 = self.helper(s,i,i)
# if maxlen1>maxlen:
# maxlen =maxlen1
# left =left1
# right =right1
# if s[i] ==s[i+1]:
# left2,right2,maxlen2 = self.helper(s,i,i+1)
# if maxlen2 >maxlen:
# maxlen =maxlen2
# left = left2
# right = right2
# return s[left:right+1]

# # #回文会有奇数和偶数长度的情况，我们都需要检测，并且存入最大的长度和其对应的left，right的坐标
# # maxlen =0
# # left =0
# # right =0
# # for i in range(len(s)-1): #这里-1是为了偶数中心永远不过过结。不然偶数中心到了最后了还会往后占一位，这会导致超出定义域
# # # 检测奇数的情况
# # left1,right1, maxlen1 = self.ispal(s, i,i)
# # if maxlen1>maxlen:
# # maxlen =maxlen1
# # left =left1
# # right =right1
# # #检测偶数的情况！！！这里必须注意，要这一位和下一位相同才能进入
# # if s[i] == s[i+1]:
# # left2,right2, maxlen2 = self.ispal(s, i,i+1)
# # if maxlen2>maxlen:
# # maxlen =maxlen2
# # left =left2
# # right =right2
# # #最后返回对应的位置的圈出来的字符
# # return s[left:right+1]

        