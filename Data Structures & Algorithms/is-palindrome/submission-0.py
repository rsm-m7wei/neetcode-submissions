class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1 确保是字母或者数字
        # 转化为小写
        #检查对应位置是不是一样的
        #首先写出1的函数
        ## 每一个def下面都必须有一个代码块，不想写的话，可以留一个pass
        i =0 
        j = len(s)-1
        while i<j:
            while not self.alphanum(s[i]) and i<j:
                i+=1
            while not self.alphanum(s[j]) and j>i:
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True
    def alphanum(self,c):
        return(ord('a')<=ord(c)<=ord('z') or ord('A')<=ord(c)<=ord('Z') or ord('0')<=ord(c)<=ord('9'))

       