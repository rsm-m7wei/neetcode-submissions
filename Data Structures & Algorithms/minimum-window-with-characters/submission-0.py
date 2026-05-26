class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        need = len(countT) # t中不同字符的种类数量，用于判断窗口是否已经满足所有目标字符的需求
        have = 0
        l = 0
        res = [-1, -1]
        reslen = float("inf")

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # 只有当某字符在窗口中的数量“达到需求”时，才计入 have
            if c in countT and window[c] == countT[c]:
                have += 1

            # 满足所有需求后，尽量收缩左边界并更新答案
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if reslen != float("inf") else ""
