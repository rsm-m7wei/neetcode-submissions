class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初始化左右指针
        # l 表示买入日（left），r 表示卖出日（right）
        l = 0
        r = 1
        
        # 记录当前为止的最大利润
        maxp = 0

        # 当右指针还没有到达最后一天之前，一直循环
        while r < len(prices):
            
            # 如果当前卖出价格比买入价格高 → 有可能赚钱
            if prices[r] > prices[l]:
                # 计算当前利润
                profit = prices[r] - prices[l]
                # 更新最大利润
                maxp = max(maxp, profit)
            else:
                # 如果价格下降（无法赚钱）
                # 那么把买入日移动到当前日（因为更便宜）
                l = r
            
            # 无论如何，卖出日都往右移一格
            r += 1
        
        # 返回最终能获得的最大利润
        return maxp
