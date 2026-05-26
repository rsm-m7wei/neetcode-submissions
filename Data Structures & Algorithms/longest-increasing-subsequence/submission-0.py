class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #最开始我们初始化状态，需要一个list来记录数据，一个数字来记录最长的长度
        lisnum= [nums[0]]
        maxlen =1
        #!!!比较最后一位和我们目前选取的数字的大小，大的话就append
        for i in nums[1:]:
            if i >lisnum[-1]:
                lisnum.append(i)
                maxlen +=1
                #如果小yu最后一位，就把对应位置替换掉，代表第i号位置最小能用数字几填充
            else:
                #用二分法来找到对应的位置
                left = 0
                right =len(lisnum)-1
                #!!!要确保满足基本条件
                while left<right:
                    mid =(left+right)//2
                    #如果中间点比目标大，就缩小右边
                    if lisnum[mid]>=i:
                        right = mid
                    else:
                        left =mid+1
                lisnum[left]=i
        return maxlen
                



