class Solution:
    def cycle(self, seen, course,prereq):
        if course in seen:
            return True #如果我现在要学的课程就是的前置课程里面就有我要学的课程，则存在cycle
        seen.add(course) #没有的话就把它加入到路径里面
        for p in prereq[course]: #再对我现在课程的前置课程看有没有cycle
            if self.cycle(seen,p,prereq):
                return True
        prereq[course] = [] #检查了这个课程不存在cycle之后我就可以把他的的前置课程重制为[]来剪枝
        seen.remove(course)  #并且把它踢出我们目前的路径，也就是回溯
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict 
        prereq = defaultdict(list) # 初始化一个有默认数值的list
        for c, p in prerequisites: #并且把每个课程作为ley，他的pre作为val放到一个list里面
            prereq[c].append(p)
        seen =set() # 创建一个seen的set，代表每个每个课程的前置学习路径，类似树状图里面的一条路径
        for cours in range(numCourses): 
            # 写一个检测是有否有环的函数，有的话就返回false
            if self.cycle(seen,cours,prereq):
                return False
        return True # 没有的话就返回true