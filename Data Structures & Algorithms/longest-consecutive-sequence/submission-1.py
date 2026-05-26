class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numsset= set(nums) # set化去重复
        # longest = 0 #初始化目标，也就是最长的连续数字
        # for i in numsset: # 对于里面的每一个数字
        #     if i-1 not in numsset: #我们首先要找到的是一串数字的开头，那怎么确定开头呢？如果它-1的数字没在数组里面它就是一个开头
        #         length =1 # 此时就可以初始化此时的长度是1
        #         while i + length in numsset: # 那此时就可以+1，+2，+3一点点的试探出来最大的length
        #             length +=1 
        #         longest=max(longest, length) # 取出最大的数字
        # return longest # 返回最大的数字

        setnum = set(nums)
        longest =0
        for i in setnum:
            if i-1 not in setnum:
                length =1
                while i+length in setnum:
                    length +=1
                longest =max(longest, length)
        return longest