"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #首先处理特殊情况
        if not intervals:
            return 0
        # 按会议开始时间排序，按时间顺序处理会议，才能正确判断哪些会议室已空出
        #每一次我都需要吧会议放到一个房间里面，但是如果这个房间正在使用，我就不清空它，直接放
        # 用最小堆存放当前占用会议室的结束时间，方便快速找到最早空出的会议室
        #这里heap的len就代表占用的会议室的数量

        #首先要使用heap先import
        import heapq
        #!!!!我们对intervals先排序一下(按照开始时间)注意这里不是list套list而是自己定义的数据结构，所以要明确变量
        intervals.sort(key=lambda x: x.start)
        #接着初始化房间数量的计数和heap
        maxroom =1
        #heap 先存入第一个会议的结束时间，之后从第二个开始比较
        heap = []
        heapq.heappush(heap, intervals[0].end)
        #!!!!这里也是要写清楚数据结构的变量
        for Interval in intervals[1:]:
            if Interval.start>= heap[0]:
                #如果上一个会议在下一个会议（已经根据开始时间排序过）开始之前就结束了，则可以继续用这个房间
                heapq.heappop(heap)
            #不管是是否弹出出都要找一个房间放下当前会议，也就是更新结束时间
            #!!!要写清楚数据结构
            heapq.heappush(heap,Interval.end)
            #并且更新 maxroom
            maxroom =max(maxroom, len(heap))
        return maxroom



        
