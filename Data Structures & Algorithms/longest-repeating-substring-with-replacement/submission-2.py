class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count = {}#计数器
        # l = 0
        # res= 0
        # maxf= 0
        # for r in range(len(s)):
        #     count[s[r]] =1+count.get(s[r],0) # 计数
        #     maxf= max(maxf,count[s[r]]) #取出目前重复最多的数字得频率
        #     while (r-l+1)-maxf>k: #如果不满足的情况下需要左边缩短，并且去左边的字母
        #         count[s[l]] -=1
        #         l+=1
        #     res = max(r-l+1,res) #计算最大的窗口
        # return res

        #初始化我们见过的东西的储存器，这里要储存见过什么以及出现的次数，所以我们用字典
        #以及左边指针，最大值，以及目前的见到的最长的重复字数
        # l =0
        # res =0
        # maxs =0
        # count ={}
        # #遍历右指针
        # for r in range(len(s)):
        #     #把它加入已经见过的加一，没有就初始化一个
        #     count[s[r]] =count.get(s[r],0)+1
        #     #加入当前字母之后再比较，看看是不是最大值，是的话就更新
        #     maxs =max(maxs,count[s[r]])
        #     #因为我们最多只能替换k个字母，所以不满足的话，我们要缩小左边窗口
        #     while r-l+1-maxs>k:
        #         count[s[l]]-=1
        #         l+=1
        #     #没有重复的时候更新最大长度
        #     res = max(res,r-l+1)
        # return res

        seen ={}
        maxs = 0
        res=0
        l =0
        for r in range(len(s)):
            seen[s[r]] =seen.get(s[r],0)+1
            maxs =max(maxs,seen[s[r]])
            while r-l+1-maxs>k:
                seen[s[l]] -=1
                l+=1
            res =max(res,r-l+1)
        return res

