class Solution:
    def pali(self, s, left,right):
        count =0 
        # 如果检查的是 s[left] == s[right]，只需 right < len(s)；
        # 如果要访问 s[left-1] 或 s[right+1]，必须用 right < len(s)-1 防止越界。
        # if 只检查当前一层是否是回文；while 会不断向两边扩展，找出更大的回文。
        while left>=0 and right<len(s) and s[left] == s[right]:
            count+=1
            left -=1
            right+=1
        return count
    def countSubstrings(self, s: str) -> int:
        #定义变量来储存最终的结果
        counts =0
        for i in range(len(s)):# 遍历这里面的每一个元素
            #查看奇数的回环，并且更新counts
            counts += self.pali(s,i,i)
            #查看偶数的回环，并且更新counts
            

            counts += self.pali(s,i,i+1)
        return counts 
            