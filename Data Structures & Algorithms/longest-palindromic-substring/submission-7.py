class Solution:
    def ispalin(self,s,left,right):
        #is in range and qualify question rule
        #right cna only be last 2 position because we need check i+1 and i are the same
        while left<=right and left>0 and right <len(s)-1 and s[left-1] ==s[right+1]:
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
        for i in range(len(s)-1):
            #we check if this alpha potion ca be a palinfrommic
            left1,right1,maxlen1 = self.ispalin(s,i,i)
            if maxlen1>maxlen:
                maxlen =maxlen1
                left =left1
                right =right1
            #if i and i+1 are the same,we have additional check
            if s[i] ==s[i+1]:
                left2,right2,maxlen2 = self.ispalin(s,i,i+1)
                if maxlen2>maxlen:
                    maxlen =maxlen2
                    left =left2
                    right =right2
        return s[left:right+1]




       
        