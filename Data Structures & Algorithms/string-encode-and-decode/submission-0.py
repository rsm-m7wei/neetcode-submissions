class Solution:

    def encode(self, strs: List[str]) -> str:
        s =""
        for k in strs: 
            s += str(len(k))+'#'+k # 这里的str是不包括全部的，不然就会先计算这里面的东西，也就是先让数字和字符串想家，这样就会报错，而只需要把数字转化成字符串才行
        return s # 写完代码最后别忘了return 
    def decode(self, s: str) -> List[str]:
        res= []
        i = 0 # 根据题目要求，需要输出是一个list，所以你需要一个了ist来装这里面的东西，同时初始化一个指针
        while i < len(s):
            j=i
            while s[j] !='#': # 寻找#,注意这里是取出字符串里面的对应数字所以要用的是[j],不能直接写j， 来确定 length，并注意要把它转化为数字类型才能寻找这里面的对应字符
                j+=1
            length =int(s[i:j])
            res.append(s[j+1:length+1+j])# 注意变量的类型
            i = j+length+1 # 最后别忘了更新指针
        return res



        s= ""
        for k in strs :
            s = s+str(len(k))+'#'+k
        return s

        res=[]
        i = 0
        while i<len(s):
            j= i
            while j!= '#':
                j+=1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i =j+length+1
        return 








