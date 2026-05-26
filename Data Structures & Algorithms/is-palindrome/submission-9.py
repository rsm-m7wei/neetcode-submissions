class Solution:
    # def isalp(self,c):
    #     return ord('a')<=ord(c)<=ord('z') or ord('A')<=ord(c)<=ord('Z') or ord('0')<=ord(c)<=ord('9')

    def isalp(self, c):
        return (ord('a')<=ord(c)<=ord('z') or ord('A')<= ord(c)<= ord('Z') or ord('0')<= ord(c)<= ord('9'))
    

    def isPalindrome(self, s: str) -> bool:
        # 1 确保是字母或者数字
        # 转化为小写
        #检查对应位置是不是一样的
        #首先写出1的函数
        ## 每一个def下面都必须有一个代码块，不想写的话，可以留一个pass
    #     i =0 
    #     j = len(s)-1
    #     while i<j:
    #         while not self.alphanum(s[i]) and i<j:
    #             i+=1
    #         while not self.alphanum(s[j]) and j>i:
    #             j-=1
    #         if s[i].lower() != s[j].lower():
    #             return False
    #         i+=1
    #         j-=1
    #     return True
        # 
        
        #用两个指针从左边和右边同时推进，向中间一个个 判断 1 是不是在范围之内 2 是不是一样的字，不是的话就返回false，是的话就下一个
        i =0
        j =len(s)-1
        while i<j:
            #每一个我们变化之后可能会越界，所以还是需要判断ij,并且这里是跳过的情况
            while i<j and not self.isalp(s[i]):
                i+=1
            while i<j and not self.isalp(s[j]):
                j-=1
            #除掉了不是范围内的数值
            #判断是否相等
            if s[i].lower() != s[j].lower():
                return False
            #如果两个相等就移动到下一个位置
            i+=1
            j-=1
        #最后都运行完了，没有错了就return true
        return True
        
            
        
            
    # def alphanum(self,c):
    #     return(ord('a')<=ord(c)<=ord('z') or ord('A')<=ord(c)<=ord('Z') or ord('0')<=ord(c)<=ord('9'))

    #写一个辅助函数去报是有效字符，由于不检查大小写，后续还要自己检查

       