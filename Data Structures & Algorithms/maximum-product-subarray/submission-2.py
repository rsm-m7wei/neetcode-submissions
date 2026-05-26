class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #首先我们初始化两个数字来记录最大和最小值，因为最小值如果遇到负数就会变为最大值
        maxn=minn = nums[0]
        #接着创建一一个变量来存放全局出现过的最大的数字
        maxall =maxn
        #我们已经处理了第一位，所以可以从第二位开始
        for i in nums[1:]:
            #首先处理最大或者最小都行，但是得先把另一个放到变量里面存起俩，不然后续就变了
            temp = maxn
            #要么这里重新开始，要么和前面的乘在一起
            maxn = max(i, maxn*i, minn*i)
            minn= min(i, temp*i, minn*i)
            #别忘了也要更新maxall
            maxall =max(maxall,maxn)
        return maxall

            
