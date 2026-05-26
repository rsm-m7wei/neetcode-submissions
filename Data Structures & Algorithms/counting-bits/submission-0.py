class Solution:
    def countBits(self, n: int) -> List[int]:
       # 创建一个存放了0的对应1数目的列表
        res= [0]
        #range时不包括最后的，所以我们需要+1
        for i in range(1,n+1):
            # 对偶数来说每一个数的i数值和除2的数的i数值是一样的，如果是遇到奇数，加一个1就行
            res.append(res[i//2]+i%2)
        return res