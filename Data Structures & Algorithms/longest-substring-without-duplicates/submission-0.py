class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 用一个 set 来记录当前窗口中出现过的字符
        # set 查找和删除都是 O(1)，非常高效
        charset = set()

        # 左指针 l 表示当前窗口的起始位置
        l = 0

        # res 用来记录最长子串的长度
        res = 0

        # 右指针 r 从 0 开始遍历字符串 s
        for r in range(len(s)):

            # 如果 s[r] 已经在当前窗口中，说明出现重复字符
            # 我们就要不断移动左指针 l，直到窗口中没有重复字符
            while s[r] in charset:
                charset.remove(s[l])  # 移除左边字符
                l += 1                # 左指针右移，缩小窗口

            # 把当前字符加入窗口（现在已保证无重复）
            charset.add(s[r])

            # 计算当前窗口长度（r - l + 1），更新最大长度
            res = max(res, r - l + 1)

        # 遍历结束，res 就是最长无重复子串的长度
        return res

        l = 0
        resset =set()
        res= 0
        for r in range(len(s)):
            while s[r] in resset:
                resset.remove(s[l])
                l+=1
            resset.add(s[r])
            res = max(res, r-l+1)
        return res
