class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 这里强调了只差了一个数字，所以我们可以如此简化
        # 根据题目我们假设他是完整的并且求和，之后减去现在有的数字的和，就可以得到差的
        return (len(nums)*(len(nums)+1)//2) -sum(nums)