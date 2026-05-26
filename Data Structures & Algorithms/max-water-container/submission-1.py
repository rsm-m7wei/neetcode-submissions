class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        【题目目标】
        给定一组竖线的高度 heights[i]，每条线在坐标 i 处，
        任意两条线与 x 轴可以组成一个“容器”，容器能装的水量是：
            area = min(heights[i], heights[j]) * (j - i)
        要求返回能装的最大水量。

        【算法核心】
        使用「双指针」法在 O(n) 时间内找到最大面积。
        关键思想：
            - 面积取决于“短板”。
            - 先从两端开始，向中间收缩。
            - 每次移动短板，尝试寻找更高的边。
        """

        # s = 0                 # 当前已找到的最大装水面积
        # l = 0                 # 左指针，从最左边的线开始
        # r = len(heights) - 1  # 右指针，从最右边的线开始

        # # 当左右指针没有相遇时，循环继续
        # while l < r:
        #     # 当前容器的高度取决于较短的一边
        #     height = min(heights[l], heights[r])
        #     width = r - l
        #     area = height * width  # 当前容器的装水量

        #     # 更新最大值
        #     s = max(s, area)

        #     # 移动较短的那一边：
        #     # 因为面积由短板决定，移动长板不会提高高度，
        #     # 只能缩小宽度 → 面积只会更小。
        #     # 所以要尝试移动短的一边，看能否找到更高的边。
        #     if heights[l] < heights[r]:
        #         l += 1
        #     else:
        #         r -= 1

        # return s  # 返回最大装水量


        #初始化一个变量存面积
        s=0
        #初始化左右两个指针
        l=0
        r =len(heights)-1
        #如果指针有效的话
        while l<r:
            #首先计算接出来的雨水
            rain =(r-l)*min(heights[l],heights[r])
            #更新全局最大雨水数值
            s =max(s,rain)
            #之后根据指针高度来更新
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return s

