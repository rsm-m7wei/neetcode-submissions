class Solution:
    def ispalin(self,s,left,right):
        #初始化我们每一次的count的变量，并且因为这里本身也被视作回文，所以我们判断的是left 和right而不是left-1和right+1
        count=0
        while left>=0 and right<len(s) and s[left] ==s[right]:
            count+=1
            left-=1
            right+=1
        return count



    
    def countSubstrings(self, s: str) -> int:
        #我们要全局的计算count，这里重新写一个counts来记录
        counts=0
        for i in range(len(s)):
            counts+=self.ispalin(s,i,i)
            counts+=self.ispalin(s,i,i+1)
        return counts
       
            