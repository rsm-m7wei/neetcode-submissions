"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 按照开始时间来排序（因为这个sort默认的是一第一个元素来排序）
        # 这里的key= 的意思是按照什么来排序
        #lambda的意思其实和def一样，后续就是：之前是输入，：之后是输出
        #这里的i是：依次把列表中的元素传给 key 函数（你的 lambda），用返回的值作为排序依据。
        intervals.sort(key = lambda i: i.start)
        # 初始一个比起始时间点更小的end time来确保更新正确
        for i in range(1,len(intervals)):
            if intervals[i].start <intervals[i-1].end:
                return False
        return True

            