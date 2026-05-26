class Solution:
    #和问题一一样，我们写出能抢到的最大数量的的函数
    def robmax(self, nums):
        for i in range(1,len(nums)):
            if i ==1:
                nums[i]=max(nums[0],nums[1])
            else:
                nums[i] =max(nums[i]+nums[i-2],nums[i-1])
        return nums[-1]
    def rob(self, nums: List[int]) -> int:
        #这道题目由于是闭环，我们就需要分类讨论，如果我们选择抢最开始的，就不能抢最后的，反之亦然
        #如果只有一个的话，我们就只返回这一个的数值即可
        if len(nums)==1:
            return nums[0]
        else:
            return max(self.robmax(nums[1:]), self.robmax(nums[:-1]))
        