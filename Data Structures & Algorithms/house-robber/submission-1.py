class Solution:
    def rob(self, nums: List[int]) -> int:
        # for i in range(1,len(nums)):
        #     # 因为第一个就是一定是自己，不需要更新，我们从第二个开始考虑,只有两个的时候取两个里面的大头
        #     if i ==1:
        #         nums[i] =max(nums[0],nums[1])
        #     #当有三个的时候，如果我们要选择偷当前，则需要放弃前一个位置所能偷到的累积的财富，获得当前财富加上n-2点位能获得的累积最大财富
        #     #！！！ 当前点位之前的点其实都不再代表其点位的财富，而是代表该点位之前到该点位能获得的财富累积（动态规划）
        #     if i >=2:
        #         nums[i]=max(nums[i]+nums[i-2],nums[i-1])
        # #最后我们返回抢完这一条街能获得的累积财富就行
        # return nums[-1]

        #这道题我们on遍历，现在数组里面每个点的意思变了，是在这个点能得到的最大的金额的意思
        #分类讨论，如果只有一个人，我们不需要更新，就本身，如果是两个，就只需要返回两个里面最大的
        #如果有更多，则每一个点的最大数值是当前加-2或者-1，我们遍历到数列尾部即可
        for i in range(1,len(nums)):
            if i == 1:
                nums[i] =max(nums[0],nums[1])
            if i>=2:
                nums[i] =max(nums[i-1],nums[i]+nums[i-2])
        return nums[-1]