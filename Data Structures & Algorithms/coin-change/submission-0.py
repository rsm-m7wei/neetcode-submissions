class Solution:
    def helper(self,coins,amount):
        #首先处理特殊情况，如果在memo里面已经有了对应想要的数值，我们之内返回
        if amount in self.memo:
            return self.memo[amount]
        #如果不在的话，我们就递归的来找，但是之前，要设置一个inf来确保后面能更新
        min_coin = float('inf')
        for coin in coins:
            if coin <= amount:
                coin_need = self.helper(coins, amount-coin)
                #每一个都要更新这个需要的最小数量，并且我们也需要更新memo来提高速度
                
            #如果这是一个有效的更新，也就是不是inf的话，我们就可以再+1返回到上一层，
                if coin_need != float('inf'):
                    min_coin =min(coin_need+1, min_coin)
        self.memo[amount] = min_coin
        return min_coin
            

                
    def coinChange(self, coins: List[int], amount: int) -> int:
        #首先，动态规划，我们设置一个全局字典来储存一些基础的（辅助函数要用），已经知道的情况
        self.memo= {}
        #组成0只能用0个硬币
        self.memo[0] = 0
        for i in coins:
            if i <= amount:
                #在有对应硬币的情况下只放一个硬币就足够
                self.memo[i]=1
        #接下来对硬币排序，我们用最小的硬币找到大的路径，接下里在用大的硬币来优化这个路径，才能有效的更新
        coins.sort()
        #对于每一个数值，我们怎么找到其最小路径，我们写一个回溯的function来做这个
        #并且最后返回一个value
        value =self.helper(coins, amount)
        #最后如果没找到返回的会是正无穷大时根据题目意思我们要返回的是-1
        #接下来向上写一个helper function

        if  value == float('inf'):
            return -1
        else:
            return value

        