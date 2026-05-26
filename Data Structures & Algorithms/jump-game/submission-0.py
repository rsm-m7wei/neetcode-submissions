class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #首先，我们初始目前能走到的最大距离
        right =0
        last = len(nums)-1
        #接着我们判断，是不是在最大距离之内呢？在的话，我们就能到达，且比较，更新所能到达的最大距离，
        #不在的话，我们就返回false
        #最后如果最大距离大于list长度我们就返回true
        for ind, num in enumerate(nums):
            if ind > right:
                return False
            #在能达到且加上来会大于原来的最大距离的的情况下更新最大距离
            if ind +num> right:
                right =ind+num
            #大于list长度的时候返回true
            if right >= last:
                return True