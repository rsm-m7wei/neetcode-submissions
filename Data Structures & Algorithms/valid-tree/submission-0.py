class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
     

        from collections import defaultdict
        # 创建一个dict，key存放课程，value存放对应的链接信息,list形式
        link =defaultdict(list)
        #把edges里面每一个小list的信息都存进去
        for i,j in edges:
            link[i].append(j)
            #这里append是类，要加小点和（）
            link[j].append(i)
        #创建一个set来记录路径
        visited =set()
        #写一个函数，检测是不是有环？
        
        #这里是内部函数，所以之前定义过的变量不用再写一遍，并且也不需要写self，只需要写新的变量即可，也就是能定位到现在的位置的变量
        #这里我需要现在和上一个的位置，后续避免一直重复
        def cycle(curr, prev):
            #如果过去的路径里面有过我现在访问的节点的话，就存在环，也就返回true
            if curr in visited:
                return True
            #不存在的话就加入到我的路径里面
            visited.add(curr)
            for i in link[curr]:
                #对目前节点里面有链接的节点都进行检查
                #如果检查到的是上一个节点0——》1。 1——〉0这种，就跳过
                if i ==prev:
                    continue
                #如果检查之后不是以上这种情况么就正常的检查有没有cycle
                if cycle(i,curr):
                    return True
            #如果所有都遍历完，都没有检测出来环，就返回false
            return False
        #这里如果没有检测到环，并且我走过的点和数量和题目给的树的节点数量一致就返回true
        #也就是只有一棵树，而不是多棵树，中间有中断的那种
        return  not cycle(0,-1) and n ==len(visited)
            




        
                
               