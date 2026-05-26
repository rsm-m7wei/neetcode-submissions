class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #这道题还是dp这样的每次看一步和最小运动，之后我们确定起始状态和边界条件
        #创建一个空的list来存放回答
        res =[]
        #储存目标的状态
        left = newInterval[0]
        right = newInterval[1]
        length = len(intervals)
        #!!别忘来还要存起始指针来确定对于 intervals 的位置
        ind = 0
        #接下里来分类讨论：目标集在当前指向集合的左边，交集，左边？
        #！！！我们需要确保满足基本条件，也就是在边界之内
        #在右边（＜＝的话就要写len-1）
        #！！！这里从左到右处理（从小到大），用while，也就免去了for if的烦恼
        while ind< len(intervals) and intervals[ind][1]<left:
            res.append(intervals[ind])
            ind +=1
            #!!注意这里判断条件要加上等于才满足题目的意思
        while ind< len(intervals) and intervals[ind][0]<=right:
            left= min(intervals[ind][0], left)
            right = max(intervals[ind][1],right)
            ind +=1
        #最后的都处理完了再append
        res.append([left,right])
        #接下来就只剩一种情况了，这
        while ind< len(intervals):
            res.append(intervals[ind])
            ind +=1
        return res
