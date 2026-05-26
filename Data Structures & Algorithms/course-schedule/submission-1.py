class Solution:
    

    def cycle(self,seen, course, prereq):
        # 4 如果这个正在检查的课程出现在我们的路径里面就返回True
        if course in seen:
            return True
        #5 如果这个课程没有出现过，就加入到路径里面
        seen.add(course)
        #接着处理里面的前置课程，对里面的课程也进行同样的操作（类似树状结构？）
        for p in prereq[course]:
            if self.cycle(seen, p, prereq):
                return True # 这里就算是前置课程出现环也要返回true
        #如果遍历完都没有找到环，这个就是一个好节点,可以吧前置课程都清零来简化
        prereq[course] = []
        #并且把它从路径里面取出，回到上一个节点
        seen.remove(course)
        return False

            

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        


        # 1 初始化一个自动字典，value里面放list，key里面放对应的课程
        from collections import defaultdict
        prereq = defaultdict(list)
        for c,q in prerequisites:
            prereq[c].append(q)
        # 2 初始化一个set来记录路径
        seen =set()
        #3 对于里面的每一个课程都检测有没有cycle，有的话返回False，全部检测完就返回true
        for i in range(numCourses):
            if self.cycle(seen,i,prereq):
                return False
        return True


         