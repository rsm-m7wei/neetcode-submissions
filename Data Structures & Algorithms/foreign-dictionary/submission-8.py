class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #对于里面出现的每一个字母都先建立一个字典，来记录可能的方向和子字母
        adj ={c:set() for w in words for c in w}
        #按照顺序取出两两相邻的word，并且我们需要先确定一种错误情况
        for i in range(len(words)-1):
            word1,word2 =words[i],words[i+1]
            minlen =min(len(word1),len(word2))
            if len(word1)>len(word2) and word1[:minlen] == word2[:minlen]:
                return ''
            #好，确定完不是错误情况之后我们按照规则，找到这一组的顺序
            for j in range(minlen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    #找到之后我们对于剩下的字母就可以不用管了，没用
                    break
        visited ={} # 这里true代表在 current path里面，再遇到就是有环，也是一种错误，false代表我们visited过了，但是已经退回这个节点之前了
        res =[]
        #基本情况：有环，不用dfs了，返回‘’
        def dfs(c):
            if c in visited:
                return visited[c] # 这里有环，我们先返回true，后续在外层会转化为‘’

            #没有的话，就把它mark为true，并且对set里面的子节点都dfs
            visited[c] =True
            for i in adj[c]:
                if dfs(i):
                    return True # 对里面的子节点也是一样的，如果有环返回true
            #走完都没有，在归的阶段一步步加入到res里面，并且标记为false
            visited[c] =False
            res.append(c) #这里其实是从末尾到开始的顺序加入到res里面，来防止有多条路径产生歧义
            
        for c in adj:
            if dfs(c):
                return '' #对adj里面的每一个都调用dfs，任意一个发现有环，都返回空集
                    
        res.reverse() # 反转目前有的字母
        return ''.join(res) # 把它按要求输出
