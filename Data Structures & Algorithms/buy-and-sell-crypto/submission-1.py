class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # 初始化左右指针
        # # l 表示买入日（left），r 表示卖出日（right）
        # l = 0
        # r = 1
        
        # # 记录当前为止的最大利润
        # maxp = 0

        # # 当右指针还没有到达最后一天之前，一直循环
        # while r < len(prices):
            
        #     # 如果当前卖出价格比买入价格高 → 有可能赚钱
        #     if prices[r] > prices[l]:
        #         # 计算当前利润
        #         profit = prices[r] - prices[l]
        #         # 更新最大利润
        #         maxp = max(maxp, profit)
        #     else:
        #         # 如果价格下降（无法赚钱）
        #         # 那么把买入日移动到当前日（因为更便宜）
        #         l = r
            
        #     # 无论如何，卖出日都往右移一格
        #     r += 1
        
        # # 返回最终能获得的最大利润
        # return maxp

        #初始化两个指针
        l=0
        r= 1
        #创建变量储存全局最大利润
        p = 0 
        while r<len(prices):
            #当利润是正数的时候更新利润，如果是负数的话把左指针换到右指针位置，这样可能利润会更大
            if prices[r]>=prices[l]:
                cp =prices[r]-prices[l]
                p =max(p,cp)
            else:
                l =r
            #无论是哪种情况最后我们都要向右移动右指针
            r+=1
        #最后返回全局最大利润
        return p

