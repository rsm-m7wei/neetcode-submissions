class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #这里我们需要考虑，每一个整体的排序以及每一个的头尾是否有重叠
        #对此我们可以说首先使用sort，默认用里面每一个小list的第一个元素排序
        #这样我们既完成了小部分的整体的排序也完成了头部的排序
        #接着我们只需要考虑，尾部是需要连在一起还是分开就行

        #首先考虑特殊情况，空集或者不存在
        if  not intervals or intervals == []:
            return []
        #！！首先初始化一些我们需要的东西
        #存放回答的list
        res =[]
        intervals.sort()
        for interval in intervals:
            #首先考虑直接放进去的情况：作为第一个或者没有交集(起点大于res最后一个的末尾)
            if res ==[] or interval[0]>res[-1][1]:
                res.append(interval)
            #或者就是有交集：!!此时由于之前已经给每个的起点排序过，只需要处理结尾就行
            else:
                res[-1][1] =max(res[-1][1],interval[1] )
        return res


