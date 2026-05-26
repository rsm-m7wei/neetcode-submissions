class Solution:
    

    # def cycle(self,seen, course, prereq):
    #     # 4 如果这个正在检查的课程出现在我们的路径里面就返回True
    #     if course in seen:
    #         return True
    #     #5 如果这个课程没有出现过，就加入到路径里面
    #     seen.add(course)
    #     #接着处理里面的前置课程，对里面的课程也进行同样的操作（类似树状结构？）
    #     for p in prereq[course]:
    #         if self.cycle(seen, p, prereq):
    #             return True # 这里就算是前置课程出现环也要返回true
    #     #如果遍历完都没有找到环，这个就是一个好节点,可以吧前置课程都清零来简化
    #     prereq[course] = []
    #     #并且把它从路径里面取出，回到上一个节点
    #     seen.remove(course)
    #     return False

    def loop(self, prereq,seen,i):
        #基本情况：如果seen里面有当前处理的课程就返回true，代表有loop
        if i in seen:
            return True
        #没有的话就加入到seen里面
        seen.add(i)
        #并且对于每一个字典中的课程他的value里面的也是要dfs,如果有的话返回true
        for j in prereq[i]:
            if self.loop(prereq,seen,j):
                return True
        #全部检查了都没有的话，我们就要把这个课程的前置清空，来提升效率，并且把路程（seen）清空
        prereq[i]=[]
        seen.remove(i)
        #全部检查完以后没有loop的话就返回false
        return False
        

            

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #我们希望初始化一个字典，我们整理每一个课程，和他的前置课程
        from collections import defaultdict
        prereq = defaultdict(list)
        for i,j in prerequisites:
            prereq[i].append(j)
        #我们要做dfs，需要记录路径所以建立一个set来记录路径（用set效率更高）
        seen = set()
        #对prerequisites里面的咩一个都用一个dfs函数来看有没loop
        for i in range(numCourses):
            if self.loop(prereq,seen,i):
                return False
        return True



        # # 1 初始化一个自动字典，value里面放list，key里面放对应的课程
        # from collections import defaultdict
        # prereq = defaultdict(list)
        # for c,q in prerequisites:
        #     prereq[c].append(q)
        # # 2 初始化一个set来记录路径
        # seen =set()
        # #3 对于里面的每一个课程都检测有没有cycle，有的话返回False，全部检测完就返回true
        # for i in range(numCourses):
        #     if self.cycle(seen,i,prereq):
        #         return False
        # return True


         