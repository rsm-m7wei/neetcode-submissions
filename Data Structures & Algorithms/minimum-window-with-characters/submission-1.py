class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ✅ Step 1. 特殊情况处理：如果目标字符串 t 是空的，直接返回空串
        if t == '':
            return ''

        # ✅ Step 2. 初始化字典，用于统计字符出现次数
        count = {}   # 存放 t 中每个字符的目标出现次数
        window = {}  # 存放当前窗口中每个字符的出现次数

        # ⚠️ 常见错误 ①：别写成 count = count.get(c,0)+1，会把字典变成整数！
        for c in t:
            count[c] = count.get(c, 0) + 1  # 正确写法：更新字典中 key=c 的计数

        # ✅ Step 3. 初始化状态变量
        have = 0                     # 当前窗口中，已经满足需求的字符种类数
        need = len(count)            # ✅ t 中不同字符的种类数量，用于判断是否满足所有需求
        l = 0                        # 左指针，控制窗口左边界
        res = [-1, -1]               # 保存最优窗口的左右边界（初始为无效）
        reslen = float('infinity')   # ✅ 初始化最短窗口长度为“无穷大”，方便后续比较

        # ✅ Step 4. 滑动右指针，扩张窗口
        for r in range(len(s)):
            c = s[r]                                # 当前右指针指向的字符
            window[c] = window.get(c, 0) + 1        # ⚠️ 常见错误 ②：别写成 window = window.get(c,0)+1！

            # ✅ Step 5. 当当前字符 c 在目标中，并且刚好满足需求时，have + 1
            # ⚠️ 注意不是“只要遇到就加”，而是“满足需求才加”
            if c in count and window[c] == count[c]:
                have += 1

            # ✅ Step 6. 当窗口已经满足所有目标字符时（have == need）
            # 说明当前窗口是一个“可行解”，尝试收缩左边界，找更短的
            while have == need:
                # ✅ 如果当前窗口更短，更新最优解
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = (r - l + 1)

                # ✅ Step 7. 收缩窗口：移除左端字符
                window[s[l]] -= 1

                # ⚠️ 当移除的字符是目标字符，并且窗口内数量低于需求 → have 减 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1

                # ⚠️ 常见错误 ③：l += 1 一定要放在 while 内部、但在 if 外部
                # 不管是否满足条件，都要移动左指针，否则会死循环！
                l += 1

        # ✅ Step 8. 提取最优结果的左右边界
        l, r = res

        # ✅ Step 9. 返回最终结果
        # ⚠️ 常见错误 ④：不能写成 res[l:r+1]，res 是索引，不是字符串！
        # 如果没找到有效窗口（reslen 仍为无穷大），返回空字符串
        return s[l:r+1] if reslen != float('infinity') else ''
