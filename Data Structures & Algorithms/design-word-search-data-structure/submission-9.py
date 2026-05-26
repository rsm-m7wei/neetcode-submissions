# class TrieNode:
#     def __init__(self):
#         # self.children ={}
#         # self.word =False

#this question does not provide the data structure so we have to make it out self
class Trienode:
    def __init__(self):
        self.children ={}
        self.word =False

        
class WordDictionary:
    def __init__(self):
    #    self.root = TrieNode()
   
    #beacuse it is in another class and we want oconnect the defalt function in another class
    #Trienode相当于是一个蓝图，Trienode（）代表按照蓝图开始建造一个房子，本来是空的
    #但是具体怎么操作？看里面的函数，__init＿ 是他会自动运行的默认初始函数，
    #这里面self.children 里面的self就代表Trienode 本身，我本把它拿过来分配一块地叫做children，并且放入{}
        self.root = Trienode()

    def addWord(self, word: str) -> None:
        #初始化位置到根节点
        curr = self.root
        for i in word:
            if i not in curr.children:
                #没有的情况下加入当前字
                curr.children[i] = Trienode()
            #把当前的指针移动到下一个目标
            curr = curr.children[i]
        #全部都输入完之后，最后加入一个单词标签
        curr.word =True


        # curr = self.root # ！！最重要的是这只开始的起点，这样我才知道是在trienode的什么位置
        # for i in word: # 我写i来遍历，这样我也知道是在word里面的什么位置了
        #     if i not in curr.children:
        #         curr.children[i] = Trienode() # 对于不在的，在curr指向的这一层存入
        #     curr = curr.children[i] # 并且更新在整个树里面的位置，无论
        
        # curr.word = True #在最后的一个node改变word为true


    def search(self, word: str) -> bool:
        def dfs(i, curr): # 1原本我有我认得，1加上i我就可以知道确定的word的位置，而对于原来建立的树，我有了curr（）指向的根，我就知道现在处于树的什么位置
            if i == len(word):
                return curr.word # 对于 dfs 我依旧首先考虑最后的通过的条件(递归结束条件)
            if word[i] == '.': # 首先分类讨论存在的状态，再在里面写最终通过，false，和递归最后通过的逻辑
                for letter in curr.children.values(): # 如果遇到的节点是.那么就跳过这一层的判断，对这一层里面的每一派生出来的节点都进行dfs，如果有一个跑通了就返回true，全都没通就返回false
                    if dfs(i+1, letter):
                        return True
                return False
            else: 
                if word[i] not in curr.children: # 如果存在的话再判断，不存在直接返回错误
                    return False
                return dfs(i+1, curr.children[word[i]])# 这里你想找到的是children里面的word，所以你要放到一个[]里面做切片 # 对于里面的通过的元素递归判断
        return dfs(0,self.root) # 2之后我先写出最终return里面的元素，这样我能更明确的知道内部的函数该怎么写

        #！！！！ 这里在最后已经清楚的把开始的的节点传入了，所以不需要写curr =slef.root
        # ！！！ 并且这里我也可以在传入的时候i+1所以也可以不考虑遍历的问题，dfs里面存放的东西我就不用写for来遍历了
