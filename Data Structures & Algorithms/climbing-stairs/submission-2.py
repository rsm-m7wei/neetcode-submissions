class Solution:
    def climbStairs(self, n: int) -> int:
#         # 这次是斐波那契数列，我们初始一些情况，之后的只要递归到前面我们已经知道的就行
#         ways =[1,1,2]
#         for n in range(3, n+1):
#             ways.append(ways[n-1]+ways[n-2])
#         #之后我们就返回对应的位置就行
#         return ways[n]

        #依旧是递归，把后续的情况递归到前面简单的情况上面
        ways=[1,1,2]
        for n in range(3,n+1):
            ways.append(ways[n-1]+ways[n-2]) #把第四个依赖到第三个
        return ways[n]
