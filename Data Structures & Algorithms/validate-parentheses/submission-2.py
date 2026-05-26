class Solution:
    def isValid(self, s: str) -> bool:
        # # 🧩 1️⃣ 初始化一个空栈，用来存放“还没匹配的左括号”
        # stack = []

        # # 🧩 2️⃣ 建立一个映射表：每个右括号对应哪个左括号
        # # key 是右括号，value 是它对应的左括号
        # closeopen = {')': '(', ']': '[', '}': '{'}

        # # 🧩 3️⃣ 遍历字符串中的每一个字符
        # for c in s:
        #     # ✅ 判断当前字符是否是右括号
        #     # ⚠️ 注意：`if c in closeopen` 检查的是「c 是否在字典的 key 中」
        #     # 也就是判断当前字符是不是一个右括号（), ], }）
        #     # （因为右括号都在 key，左括号都在 value）
        #     if c in closeopen:
        #         # ⚠️ 访问栈顶前要确保栈不为空，否则 stack[-1] 会报错
        #         # 检查当前右括号能否与栈顶左括号匹配
        #         if stack and stack[-1] == closeopen[c]:
        #             stack.pop()        # ✅ 匹配成功：弹出栈顶左括号
        #         else:
        #             # ❌ 匹配失败的两种情况：
        #             #   1. 栈为空（还没左括号就来了右括号）
        #             #   2. 栈顶不是对应的左括号（类型不对）
        #             # 两种情况都代表非法括号序列，直接返回 False
        #             return False
        #     else:
        #         # ✅ 否则说明是左括号（左括号不在 key，而在 value）
        #         # 左括号入栈，等待后续匹配
        #         stack.append(c)

        # # 🧩 4️⃣ 所有字符都遍历完后：
        # # 如果栈为空（not stack 为 True）说明全部匹配成功；
        # # 如果栈里还有没配对的左括号，就返回 False。
        # return True if not stack else False


        # #初始化一个stack
        # stack =[]
        # #初始化一个右括号作为key的map
        # closeopen = {')': '(', ']': '[', '}': '{'}
        # #对于里面的每一个元素，如果不是右括号就加入，是的话就看是不是对应的，是就弹出，不是就false
        # for c in s:
        #     if c in closeopen:
        #         if stack and stack[-1] ==closeopen[c]:
        #             stack.pop()
        #         else:
        #             False
        #     else:
        #         stack.append(c)
        # return True if not stack else False

        #创建一个站，先检查是不是有，有的，且对的弹出，有且不对false，没有false

        stack =[]
        #创建一个字典
        closeopen = {')':'(',']':'[','}':'{'}
        for c in s:
            #左括号和右括号的逻辑不一样
            if c in closeopen:
                #确保stack里面得先有东西
                if stack and stack[-1] == closeopen[c]:
                    stack.pop()
                else:
                    return False
            #左括号的话
            else:
                stack.append(c)
                #最后stack空了就返回true，不空就返回false
        return True if not stack else False


