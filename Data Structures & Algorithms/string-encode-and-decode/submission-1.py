class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            #按照长度， 加特殊符号加原文来加密整个文字
            s+= str(len(i))+'#'+i # 注意类型转换，要是字符类型
        return s # 有输出就非常大概率有return 一定要记得写

        

    def decode(self, s: str) -> List[str]:
        res =[]
        #初始化指针，并且while手动控制进度
        i = 0
        while i<len(s):
            j=i
            while s[j]!="#": # 这里是取出字典的对应字符不是J！！！
                j+=1
            lenghth= int(s[i:j]) # 这里要注意类型转化，数字应该是int
            res.append(s[j+1:j+1+lenghth])
            i=j+lenghth+1 # 更新i到下一个数字
        return res

        




        




