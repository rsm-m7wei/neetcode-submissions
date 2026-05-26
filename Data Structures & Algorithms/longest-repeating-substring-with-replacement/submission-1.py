class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}#计数器
        l = 0
        res= 0
        maxf= 0
        for r in range(len(s)):
            count[s[r]] =1+count.get(s[r],0) # 计数
            maxf= max(maxf,count[s[r]]) #取出目前重复最多的数字得频率
            while (r-l+1)-maxf>k: #如果不满足的情况下需要左边缩短，并且去左边的字母
                count[s[l]] -=1
                l+=1
            res = max(r-l+1,res) #计算最大的窗口
        return res
        