class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        #当n 不等于0的时候
        while n:
            res += n%2 
            # n向右移动一位
            n =n>>1
        return res