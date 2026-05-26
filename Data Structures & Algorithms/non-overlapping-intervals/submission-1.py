class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 按区间结束时间排序，贪心地优先保留结束最早的区间，才能给后续区间留下最大的可选空间（全局最优）
        #首先考虑特殊情况：interval不存在或者直接就是【】
        if intervals == [] or not intervals:
            return 0
        #！！！按照结尾时间来排序
        #!!!一定要是key
        intervals.sort(key = lambda x:x[1])
        remove =0
        #初始化结尾时间，我们取得第一个区间的结尾作为结尾时间，之后从第二是开始比较，如果后面的的有重叠，就删除掉（remove +=1）
        end = intervals[0][1]

        #！！从第二个开始
        # 重叠时删除结束更晚的区间（当前区间），以给后续区间留出更多空间
        # 不重叠时保留当前区间，并更新结束时间作为新的比较基准
        #！！！ 这里不是and 是,

        for s,e in intervals[1:]:
            #有重叠的话我们就删除掉
            if s < end:
                remove +=1
            # 当前区间不与已保留区间重叠，说明可以接上它，因此更新 end 为当前区间的结束时间
            else:
                end =e
        return remove