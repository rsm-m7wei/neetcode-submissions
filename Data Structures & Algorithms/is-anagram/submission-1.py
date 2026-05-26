class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # count ={} #因为要记得对应的字母的次数，所以要用字典
        # for i in s: 
        #     count[i]= count.get(i, 0)+1#对于第一个数只需要循环记录总数就行
        # for j in t:
        #     if j  not in count: # 这里只有not in 没有is
        #         return False #对于第二个数组，如果是有新的元素直接返回f，一定不相等
        #     count[j]-=1 #在有的情况下把对应的数字减少1
        #     if count[j]== 0:  # 这里一定是== 这是用来判断TF的，如果只有一个就是赋值了
        #         del count[j] # 如果是0的话，可以选择删掉，没用了这个就
        # return len(count) == 0 # 如果删掉上面两行的话，这个就没法用了，1得用 return all(v ==0 for v in count.values())

        #思路是将一个词存入字典之中，用另一个词来消除，如果这个词没了就删除掉这个索引，最后检查字典长度

        #首先考虑是否有特殊情况？能直接判断的
        # if len(s)!= len(t):
        #     return False
        # #创建字典不要写dict！！
        # dic = {}
        # for i in s:
        #     #将这一个词存入字典!! 用get(i,0)+1 
        #     dic[i]= dic.get(i,0)+1

        # for j in t:
        #     if j not in dic:
        #         return False
        #     dic[j]-=1
        #     if dic[j]==0:
        #         #注意看这个删除是怎么写的
        #         del dic[j]
        # return len(dic) == 0



        #首先判断长短
        if len(s) != len(t):
            return False
        #创建字典,用get来统计字符频率，如果有就返回，没有默认写一个0
        dic ={}
        for i in s:
            dic[i] =dic.get(i,0)+1
        #遍历另一个字符串，有的话把它从原来的地方去除，没有的话直接返回false就行
        for j in t:
            if j not in dic:
                return False
            dic[j] -=1
            #如果最后是0的时候我们就删除这个位置
            if dic[j] ==0:
                del dic[j]
        #最后通过长度是不是等于0来判断两个字符串一不一样。
        return len(dic) ==0
        
            