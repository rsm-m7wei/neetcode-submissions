class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #这道题属于动态编程，我理解的就是递归的反过来
        #设置最开始的状态，就是包含第一个数字的状态
        #之后我们只需要考虑加入新的数字以后是从新数字重新开始，还是把它连接到之前的连续数组之中呢？
        #很明显，谁大就选谁，并且记录全局最大值
        #当前最大值
        currsum =0
        #全局最大值
        maxsum =nums[0]
        for i in nums:
            currsum =max(currsum+i ,i)
            maxsum =max(currsum, maxsum)
        return maxsum