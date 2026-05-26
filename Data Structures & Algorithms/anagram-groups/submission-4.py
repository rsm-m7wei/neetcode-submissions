class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list) #0创造一个dict来放东西,4 但是为了方便解决新词之前不再列表里面的情况，所以这里直改该用defaultdict(list),如果遇到新的词就会自动为他生成新的list
        # for s in strs: #1 对于里面的每一个词都给予一个长度26 的0 的列表
        #     c = [0]*26
        #     for i in s: #2 在对于这里面的每一个词，都改变出对应的c，做出他的哈希列表
        #         c[ord(i)-ord('a')] +=1  # 题目说了只有小写字母所以能用这个方法
        #     res[tuple(c)].append(s) #3 因为字典的key是不能改变的，所以要转变成tuple，作为key，在加入对应的value
        # return list(res.values()) # 取出这里面的values，但是题目要求输出是list类型，套上转化为list

        #创建一个默认会返回空list的字典，之后对于每一个单词永ord做差来并转化为tuple作为key，
        # res = defaultdict(list)
        # for s in strs:
        #     c = [0]*26
        #     for i in s:
        #         c[ord(i)-ord('a')] +=1
        #         #字典用append
        #     res[tuple(c)].append(s)
        #     #只要values，
        # return list(res.values())
        
        #首先创建一个磨人字典，因为输出的时候是list所以我们也用list
        res =defaultdict(list)
        #对我们里面的每一个数字我们都用ord来算出哈希值，再用哈希值作为key来储存单词
        #因为list是可变的，所以我们要用tuple来转化为不可变得
        for s in strs:
            c =[0]*26
            for i in s:
                c[ord(i)-ord('a')]+=1
            #这里是载入字典，所以使用append
            res[tuple(c)].append(s)
        #这里我们只要里面的value，并且因为输出要求是list形式，我们再套个list的壳
        return list(res.values())


